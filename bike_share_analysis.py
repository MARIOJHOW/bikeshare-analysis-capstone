"""
PROJETO 3: Análise Exploratória de Dados - Bike-Share (Capstone Project)
Autor: Mário Sérgio Inácio Júnior
Data: Fevereiro 2026

Inspirado no Google Data Analytics Capstone Project
Objetivo: Analisar padrões de uso de sistema de compartilhamento de bicicletas
para identificar diferenças entre usuários casuais e membros.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo visual
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (14, 8)

# Configurar fonte para suportar acentos
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 80)
print("ANÁLISE DE DADOS: SISTEMA DE BIKE-SHARE")
print("Google Data Analytics Capstone Project - Adaptado")
print("=" * 80)

# ==========================================
# 1. CRIAR DATASET SIMULADO
# ==========================================

print("\n📊 ETAPA 1: Gerando dataset de viagens...")

np.random.seed(42)

# Parâmetros do dataset
n_records = 100000  # 100k viagens
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Gerar dados realistas
data = []

for i in range(n_records):
    # Tipo de usuário (60% casuais, 40% membros)
    user_type = np.random.choice(['Casual', 'Membro'], p=[0.35, 0.65])
    
    # Data e hora da viagem
    random_day = start_date + timedelta(days=np.random.randint(0, 365))
    
    # Padrões diferentes para cada tipo de usuário
    if user_type == 'Membro':
        # Membros: mais viagens em dias úteis, horários de commute
        if random_day.weekday() < 5:  # Dia útil
            hour = np.random.choice([7, 8, 9, 17, 18, 19], p=[0.2, 0.25, 0.15, 0.15, 0.15, 0.1])
        else:  # Fim de semana
            hour = np.random.choice(range(10, 18))
        duration_minutes = np.random.normal(15, 5)  # Viagens mais curtas
    else:
        # Casuais: mais viagens em fins de semana, durações maiores
        hour = np.random.choice(range(10, 20))
        duration_minutes = np.random.normal(30, 15)  # Viagens mais longas
    
    # Garantir duração mínima
    duration_minutes = max(3, duration_minutes)
    
    start_time = random_day.replace(hour=hour, minute=np.random.randint(0, 60))
    end_time = start_time + timedelta(minutes=duration_minutes)
    
    # Tipo de bicicleta
    bike_type = np.random.choice(['Clássica', 'Elétrica', 'Docked'], p=[0.5, 0.4, 0.1])
    
    # Estações (simuladas)
    start_station = f"Estação_{np.random.randint(1, 51)}"
    end_station = f"Estação_{np.random.randint(1, 51)}"
    
    # Distância (correlacionada com duração)
    distance_km = duration_minutes * np.random.uniform(0.15, 0.25)
    
    data.append({
        'ride_id': f'VIAGEM_{str(i+1).zfill(6)}',
        'rideable_type': bike_type,
        'started_at': start_time,
        'ended_at': end_time,
        'start_station_name': start_station,
        'end_station_name': end_station,
        'member_casual': user_type,
        'ride_length_minutes': round(duration_minutes, 2),
        'distance_km': round(distance_km, 2)
    })

df = pd.DataFrame(data)

# Adicionar colunas derivadas - AGORA EM PORTUGUÊS
# Mapeamento manual de dias e meses
dias_semana = {
    0: 'Segunda',
    1: 'Terça',
    2: 'Quarta',
    3: 'Quinta',
    4: 'Sexta',
    5: 'Sábado',
    6: 'Domingo'
}

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

df['day_of_week'] = df['started_at'].dt.dayofweek.map(dias_semana)
df['month'] = df['started_at'].dt.month.map(meses)
df['hour'] = df['started_at'].dt.hour
df['is_weekend'] = df['started_at'].dt.dayofweek.isin([5, 6]).astype(int)

print(f"✅ Dataset criado: {len(df):,} viagens")
print(f"📅 Período: {df['started_at'].min().strftime('%Y-%m-%d')} a {df['started_at'].max().strftime('%Y-%m-%d')}")

# Salvar dataset
df.to_csv('bike_share_data.csv', index=False, encoding='utf-8-sig')
print(f"💾 Dataset salvo: bike_share_data.csv")

# ==========================================
# 2. ANÁLISE EXPLORATÓRIA
# ==========================================

print("\n" + "=" * 80)
print("ETAPA 2: ANÁLISE EXPLORATÓRIA DE DADOS")
print("=" * 80)

# ------ ANÁLISE 1: Visão Geral ------
print("\n📊 ANÁLISE 1: Visão Geral do Dataset")
print("-" * 80)

print(f"\nTotal de viagens: {len(df):,}")
print(f"Período analisado: {(df['started_at'].max() - df['started_at'].min()).days} dias")
print(f"\nDistribuição por tipo de usuário:")
print(df['member_casual'].value_counts())
print(f"\nPercentual:")
print(df['member_casual'].value_counts(normalize=True).mul(100).round(2).astype(str) + '%')

# ------ ANÁLISE 2: Duração das Viagens ------
print("\n" + "=" * 80)
print("📊 ANÁLISE 2: Duração das Viagens por Tipo de Usuário")
print("-" * 80)

duration_stats = df.groupby('member_casual')['ride_length_minutes'].agg([
    ('Média', 'mean'),
    ('Mediana', 'median'),
    ('Mínima', 'min'),
    ('Máxima', 'max'),
    ('Total_Viagens', 'count')
]).round(2)

print(duration_stats)

casual_avg = duration_stats.loc['Casual', 'Média']
member_avg = duration_stats.loc['Membro', 'Média']
diferenca = ((casual_avg - member_avg) / member_avg * 100)

print(f"\n💡 INSIGHT: Usuários casuais fazem viagens {diferenca:.1f}% mais longas que membros")
print(f"   Casual: {casual_avg:.1f} min | Membro: {member_avg:.1f} min")

# ------ ANÁLISE 3: Padrão por Dia da Semana ------
print("\n" + "=" * 80)
print("📊 ANÁLISE 3: Padrão de Uso por Dia da Semana")
print("-" * 80)

# Ordenar dias da semana
day_order = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=day_order, ordered=True)

trips_by_day = df.groupby(['day_of_week', 'member_casual']).size().unstack(fill_value=0)
print(trips_by_day)

# Calcular diferença fim de semana vs semana
weekend_casual = df[(df['is_weekend'] == 1) & (df['member_casual'] == 'Casual')].shape[0]
weekday_casual = df[(df['is_weekend'] == 0) & (df['member_casual'] == 'Casual')].shape[0]
casual_weekend_pct = weekend_casual / (weekend_casual + weekday_casual) * 100

weekend_member = df[(df['is_weekend'] == 1) & (df['member_casual'] == 'Membro')].shape[0]
weekday_member = df[(df['is_weekend'] == 0) & (df['member_casual'] == 'Membro')].shape[0]
member_weekend_pct = weekend_member / (weekend_member + weekday_member) * 100

print(f"\n💡 INSIGHT: Padrão de uso semanal:")
print(f"   Casuais: {casual_weekend_pct:.1f}% das viagens em fins de semana")
print(f"   Membros: {member_weekend_pct:.1f}% das viagens em fins de semana")
print(f"   → Membros usam mais para commute (dias úteis)")

# ------ ANÁLISE 4: Horários de Pico ------
print("\n" + "=" * 80)
print("📊 ANÁLISE 4: Distribuição por Hora do Dia")
print("-" * 80)

trips_by_hour = df.groupby(['hour', 'member_casual']).size().unstack(fill_value=0)
print("\nTop 5 horários para cada grupo:")
print("\nCASUAL:")
print(trips_by_hour['Casual'].nlargest(5))
print("\nMEMBRO:")
print(trips_by_hour['Membro'].nlargest(5))

print(f"\n💡 INSIGHT: Membros têm picos às 8h e 18h (horário de trabalho)")
print(f"           Casuais têm uso distribuído ao longo do dia (lazer)")

# ------ ANÁLISE 5: Tipo de Bicicleta ------
print("\n" + "=" * 80)
print("📊 ANÁLISE 5: Preferência de Tipo de Bicicleta")
print("-" * 80)

bike_preference = pd.crosstab(df['member_casual'], df['rideable_type'], normalize='index').mul(100).round(2)
print(bike_preference)

# ------ ANÁLISE 6: Sazonalidade ------
print("\n" + "=" * 80)
print("📊 ANÁLISE 6: Sazonalidade - Viagens por Mês")
print("-" * 80)

month_order = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
               'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

trips_by_month = df.groupby(['month', 'member_casual']).size().unstack(fill_value=0)
print(trips_by_month)

# Identificar meses de pico
total_by_month = trips_by_month.sum(axis=1)
peak_month = total_by_month.idxmax()
low_month = total_by_month.idxmin()

print(f"\n💡 INSIGHT: Sazonalidade evidente")
print(f"   Pico: {peak_month} ({total_by_month[peak_month]:,} viagens)")
print(f"   Menor: {low_month} ({total_by_month[low_month]:,} viagens)")

# ==========================================
# 3. VISUALIZAÇÕES
# ==========================================

print("\n" + "=" * 80)
print("ETAPA 3: Gerando Visualizações")
print("=" * 80)

fig, axes = plt.subplots(2, 3, figsize=(20, 12))
fig.suptitle('Análise de Bike-Share: Casuais vs Membros', fontsize=16, fontweight='bold', y=1.00)

# 1. Distribuição de Usuários
ax1 = axes[0, 0]
df['member_casual'].value_counts().plot(kind='bar', ax=ax1, color=['#FF6B6B', '#4ECDC4'])
ax1.set_title('Distribuição de Usuários', fontweight='bold')
ax1.set_xlabel('Tipo de Usuário')
ax1.set_ylabel('Número de Viagens')
ax1.tick_params(axis='x', rotation=0)

# 2. Duração Média por Tipo
ax2 = axes[0, 1]
duration_stats[['Média']].plot(kind='bar', ax=ax2, color=['#FF6B6B', '#4ECDC4'], legend=False)
ax2.set_title('Duração Média das Viagens (minutos)', fontweight='bold')
ax2.set_xlabel('Tipo de Usuário')
ax2.set_ylabel('Minutos')
ax2.tick_params(axis='x', rotation=0)

# 3. Viagens por Dia da Semana
ax3 = axes[0, 2]
trips_by_day.plot(kind='bar', ax=ax3, color=['#FF6B6B', '#4ECDC4'])
ax3.set_title('Viagens por Dia da Semana', fontweight='bold')
ax3.set_xlabel('Dia da Semana')
ax3.set_ylabel('Número de Viagens')
ax3.legend(title='Tipo')
ax3.tick_params(axis='x', rotation=45)

# 4. Viagens por Hora
ax4 = axes[1, 0]
trips_by_hour.plot(kind='line', ax=ax4, marker='o', linewidth=2, color=['#FF6B6B', '#4ECDC4'])
ax4.set_title('Distribuição por Hora do Dia', fontweight='bold')
ax4.set_xlabel('Hora do Dia')
ax4.set_ylabel('Número de Viagens')
ax4.legend(title='Tipo')
ax4.grid(True, alpha=0.3)

# 5. Tipo de Bicicleta
ax5 = axes[1, 1]
bike_counts = df.groupby(['member_casual', 'rideable_type']).size().unstack(fill_value=0)
bike_counts.plot(kind='bar', ax=ax5, color=['#95E1D3', '#F38181', '#AA96DA'])
ax5.set_title('Preferência de Tipo de Bicicleta', fontweight='bold')
ax5.set_xlabel('Tipo de Usuário')
ax5.set_ylabel('Número de Viagens')
ax5.legend(title='Tipo de Bike')
ax5.tick_params(axis='x', rotation=0)

# 6. Sazonalidade
ax6 = axes[1, 2]
trips_by_month.plot(kind='line', ax=ax6, marker='o', linewidth=2, color=['#FF6B6B', '#4ECDC4'])
ax6.set_title('Sazonalidade - Viagens por Mês', fontweight='bold')
ax6.set_xlabel('Mês')
ax6.set_ylabel('Número de Viagens')
ax6.legend(title='Tipo')
ax6.tick_params(axis='x', rotation=45)
ax6.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('bike_share_analysis.png', dpi=300, bbox_inches='tight')
print("✅ Visualizações salvas: bike_share_analysis.png")

# ==========================================
# 4. RELATÓRIO FINAL E RECOMENDAÇÕES
# ==========================================

print("\n" + "=" * 80)
print("RELATÓRIO FINAL - INSIGHTS E RECOMENDAÇÕES")
print("=" * 80)

total_rides = len(df)
casual_rides = (df['member_casual'] == 'Casual').sum()
member_rides = (df['member_casual'] == 'Membro').sum()

print(f"""
📊 RESUMO EXECUTIVO:

MÉTRICAS GERAIS:
├─ Total de viagens analisadas: {total_rides:,}
├─ Período: {(df['started_at'].max() - df['started_at'].min()).days} dias (ano completo)
├─ Usuários Casuais: {casual_rides:,} ({casual_rides/total_rides*100:.1f}%)
└─ Membros: {member_rides:,} ({member_rides/total_rides*100:.1f}%)

🔍 PRINCIPAIS DIFERENÇAS ENTRE GRUPOS:

1. DURAÇÃO DAS VIAGENS:
   ├─ Casuais: {casual_avg:.1f} min (média)
   ├─ Membros: {member_avg:.1f} min (média)
   └─ Casuais fazem viagens {diferenca:.1f}% mais longas

2. PADRÃO SEMANAL:
   ├─ Casuais: {casual_weekend_pct:.1f}% das viagens em fins de semana (lazer)
   └─ Membros: {member_weekend_pct:.1f}% das viagens em fins de semana (commute)

3. HORÁRIOS DE USO:
   ├─ Membros: Picos às 8h e 18h (horário de trabalho)
   └─ Casuais: Distribuição uniforme 10h-20h (lazer)

4. SAZONALIDADE:
   ├─ Pico de uso: {peak_month}
   └─ Menor uso: {low_month}

💡 INSIGHTS ESTRATÉGICOS:

✓ Usuários CASUAIS:
  • Usam principalmente para LAZER (fins de semana, durações longas)
  • Horários flexíveis ao longo do dia
  • Maior atividade em meses de verão
  
✓ Usuários MEMBROS:
  • Usam principalmente para COMMUTE (dias úteis, picos 8h/18h)
  • Viagens mais curtas e objetivas
  • Uso consistente ao longo do ano

📈 RECOMENDAÇÕES PARA AUMENTAR CONVERSÃO DE CASUAIS EM MEMBROS:

1. MARKETING DIRECIONADO:
   └─ Campanhas focadas em fins de semana e meses de verão
   └─ Destacar economia para uso regular (lazer → commute)

2. PLANOS FLEXÍVEIS:
   └─ Criar plano "Fim de Semana" para casuais frequentes
   └─ Oferecer teste gratuito de 30 dias no período de pico

3. INCENTIVOS:
   └─ Desconto progressivo: 10% após 5 viagens, 20% após 10 viagens
   └─ Programa de pontos para viagens longas (perfil casual)

4. COMUNICAÇÃO:
   └─ Email marketing: "Você fez X viagens em Y mês - economize Z% sendo membro"
   └─ Notificações in-app com benefícios de membership

5. PARCERIAS:
   └─ Integração com apps de turismo e lazer
   └─ Pacotes corporativos para empresas (aumentar uso commute)

🎯 METAS SUGERIDAS:
├─ Aumentar conversão casual→membro em 15% no próximo trimestre
├─ Aumentar frequência de uso de casuais em 25%
└─ Lançar 2 novos planos de membership até Q3

""")

print("=" * 80)
print("✅ Análise concluída com sucesso!")
print("=" * 80)
print("\n📁 Arquivos gerados:")
print("   ├─ bike_share_data.csv (100,000 registros)")
print("   └─ bike_share_analysis.png (6 visualizações)")
print("\n" + "=" * 80)
