# 🚴 Análise Exploratória de Dados - Sistema Bike-Share

## 🎯 Objetivo do Projeto
Conduzir análise exploratória completa de dados de sistema de compartilhamento de bicicletas para identificar padrões de comportamento entre usuários casuais e membros, fornecendo insights acionáveis para estratégias de conversão.

**Inspirado no Google Data Analytics Capstone Project**

## 📁 Estrutura do Projeto
```
projeto-bikeshare/
│
├── bike_share_data.csv              # Dataset com 100,000 viagens
├── bike_share_analysis.py           # Script completo de análise
├── bike_share_analysis.png          # Dashboard com 6 visualizações
└── README.md                        # Documentação do projeto
```

## 🔧 Tecnologias Utilizadas
- **Python 3.x**
- **Pandas** - Manipulação e análise de dados
- **NumPy** - Geração de dados simulados e cálculos
- **Matplotlib** - Visualizações
- **Seaborn** - Gráficos estatísticos aprimorados

## 📊 Dataset

**Dimensões:**
- 100.000 registros de viagens
- Período: 1 ano completo (2023)
- 9 variáveis principais

**Variáveis:**
- `ride_id` - Identificador único da viagem
- `rideable_type` - Tipo de bicicleta (Classic, Electric, Docked)
- `started_at` - Data/hora de início
- `ended_at` - Data/hora de término
- `start_station_name` - Estação de origem
- `end_station_name` - Estação de destino
- `member_casual` - Tipo de usuário (Member/Casual)
- `ride_length_minutes` - Duração da viagem
- `distance_km` - Distância percorrida

**Variáveis Derivadas:**
- `day_of_week` - Dia da semana
- `month` - Mês
- `hour` - Hora do dia
- `is_weekend` - Flag de fim de semana

## 🔍 Análises Realizadas

### 1. Visão Geral
- Distribuição de usuários (35% Casuais, 65% Membros)
- Estatísticas gerais do período

### 2. Duração das Viagens
- Comparação de tempo médio entre grupos
- **Insight:** Casuais fazem viagens 101% mais longas (30.1 min vs 15.0 min)

### 3. Padrão Semanal
- Análise de uso por dia da semana
- **Insight:** Membros concentram uso em dias úteis (commute), casuais distribuídos

### 4. Horários de Pico
- Distribuição de viagens por hora
- **Insight:** Membros têm picos às 8h e 18h; Casuais distribuem uso 10h-20h

### 5. Preferência de Bicicleta
- Análise de tipo de bike por grupo
- **Insight:** Preferência similar entre grupos (50% Classic, 40% Electric)

### 6. Sazonalidade
- Tendências mensais de uso
- **Insight:** Pico em Outubro, menor uso em Fevereiro

## 📈 Principais Descobertas

### Perfil: Usuários CASUAIS
- ✓ Viagens mais longas (média 30.1 minutos)
- ✓ Uso predominante para LAZER
- ✓ Horários flexíveis (10h-20h)
- ✓ Maior atividade em fins de semana
- ✓ Sazonalidade mais pronunciada

### Perfil: Usuários MEMBROS
- ✓ Viagens mais curtas (média 15.0 minutos)
- ✓ Uso predominante para COMMUTE
- ✓ Picos em horários de trabalho (8h, 18h)
- ✓ Maior uso em dias úteis
- ✓ Padrão consistente ao longo do ano

## 💡 Recomendações Estratégicas

### 1. Marketing Direcionado
- Campanhas em fins de semana e meses de pico
- Destacar economia em uso regular
- Foco em benefícios de membership

### 2. Novos Planos
- Plano "Fim de Semana" para casuais frequentes
- Teste gratuito de 30 dias em período de alta
- Plano corporativo para empresas

### 3. Incentivos de Conversão
- Desconto progressivo: 10% após 5 viagens, 20% após 10
- Programa de pontos para viagens longas
- Gamificação de uso

### 4. Comunicação Personalizada
- Email marketing com dados de uso individual
- Notificações in-app sobre benefícios
- Retargeting baseado em comportamento

### 5. Parcerias Estratégicas
- Integração com apps de turismo
- Parcerias com empresas locais
- Pacotes combinados (transporte + lazer)

## 🎯 Metas Propostas

- ✅ Aumentar conversão casual→membro em **15%** no próximo trimestre
- ✅ Aumentar frequência de uso de casuais em **25%**
- ✅ Lançar **2 novos planos** de membership até Q3
- ✅ Reduzir churn de membros em **10%**

## 📊 Visualizações Geradas

O projeto gera um dashboard completo com 6 visualizações:

1. **Distribuição de Usuários** (gráfico de barras)
2. **Duração Média por Tipo** (gráfico de barras comparativo)
3. **Viagens por Dia da Semana** (gráfico de barras agrupadas)
4. **Distribuição por Hora** (gráfico de linha temporal)
5. **Preferência de Bicicleta** (gráfico de barras empilhadas)
6. **Sazonalidade** (gráfico de linha mensal)

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install pandas numpy matplotlib seaborn
```

### Executar Análise Completa
```bash
python bike_share_analysis.py
```

### Saídas Geradas
- `bike_share_data.csv` - Dataset completo (100k registros)
- `bike_share_analysis.png` - Dashboard visual com 6 gráficos
- Relatório completo no terminal com insights e recomendações

## 📚 Metodologia

Este projeto segue as etapas do processo de análise de dados:

1. **Ask (Perguntar)**: Definir questão de negócio
2. **Prepare (Preparar)**: Coletar e estruturar dados
3. **Process (Processar)**: Limpar e transformar dados
4. **Analyze (Analisar)**: Identificar padrões e tendências
5. **Share (Compartilhar)**: Visualizar e comunicar insights
6. **Act (Agir)**: Recomendar ações baseadas em dados

## 🔄 Próximos Passos

- [ ] Análise de rentabilidade por tipo de usuário
- [ ] Modelo preditivo de churn
- [ ] Segmentação avançada (clustering)
- [ ] Dashboard interativo com Tableau/Power BI
- [ ] Análise de rotas mais populares
- [ ] Otimização de distribuição de bicicletas

## 👤 Autor
**Mário Sérgio Inácio Júnior**
- LinkedIn: [Mário Sérgio Inácio Júnior](https://linkedin.com/in/mário-sérgio-inácio-júnior-026705149)
- Email: mariosergioijr@gmail.com

## 📝 Notas

**Linguagem Original:** Este projeto foi desenvolvido inicialmente em R como parte do Google Data Analytics Certificate. Esta é uma versão adaptada em Python mantendo a mesma metodologia e insights.

**Ferramentas Utilizadas:**
- ✓ Python (Pandas, NumPy) - equivalente ao R/dplyr
- ✓ Matplotlib/Seaborn - equivalente ao ggplot2
- ✓ Análise estatística descritiva
- ✓ Visualização de dados

## 📄 Licença
Este projeto foi desenvolvido para fins educacionais e de portfólio.

---

*Projeto desenvolvido como parte do Google Data Analytics Capstone - Adaptado para portfólio de transição de carreira - Fevereiro 2026*
