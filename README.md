# GRA-CellTwin-Final
GRA-CellTwin-Final. What is GRA-CellTwin? GRA‑CellTwin‑Final is a multi‑level *Generalized Resonance Alignment* (GRA) simulator that creates accurate in silico replicas of single cells.  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

**In silico cell simulator for treating all diseases – built on the GRA meta-zeroing framework in a multiverse foam.**  
An open‑source counterpart to Biohub (CZI), delivering zero‑hallucination digital twins of cells.

[English](#english) | [Русский](#русский)

---

## English

### What is GRA-CellTwin?
GRA‑CellTwin‑Final is a multi‑level *Generalized Resonance Alignment* (GRA) simulator that creates accurate in silico replicas of single cells.  
It combines public transcriptomic data (CellxGene, TCGA, GEO) with a **multiverse foam** of candidate models.  
GRA zeroes out noise and hallucinations, guaranteeing ethical, explainable outputs.

### Key Concepts
- **Multiverse Foam** – a population of microscopic model bubbles, each representing a hypothetical cellular state.  
- **Critical Foam Threshold** \(\Gamma_{\text{крит}} = \min(\text{foam density}, T_c)\)  
- **Resonance Frequency** (meta‑observer) \(\omega_{\text{рез}} = \sum \Gamma_{\text{крит}} \cdot R\)  
  where \(R\) is the spatial correlation between bubbles.  
- **GRA Zeroing** – removing bubbles whose resonance deviates beyond the critical band, eliminating hallucinations.  
- **Ethics Filter** – blocks therapies that violate the "first, do no harm" principle.

### Features
- Load scRNA‑seq datasets (GEO, TCGA BRCA, CellxGene).  
- Build digital twins of diseased cells using Yamanaka factors (OSKM).  
- Generate personalised therapy: CRISPR targets, senolytics, reprogramming cocktails.  
- Interactive Jupyter notebook with Plotly trajectory graphs.  
- Integration with Ollama/LLM post‑processed by GRA to suppress hallucinations.  
- Exportable prompt for a bilingual UI on [lovable.dev](https://lovable.dev).

### Installation
```bash
git clone https://github.com/qqewq/GRA-CellTwin-Final.git
cd GRA-CellTwin-Final
pip install -r data/requirements.txt
```

### Quick Demo
```bash
jupyter notebook demos/cell_simulator.ipynb
```
Input: breast cancer → Output: OSKM + senolytics (CRISPR: TP53, MYC).

### Repository Structure
```
├── README.md
├── setup.py
├── .gitignore
├── LICENSE
├── gra_core/
│   ├── multiverse.py      # foam zeroing
│   ├── resonance.py       # ω_res calculation
│   └── ethics_box.py      # ethical filter
├── cell_models/
│   ├── cell_twin.py       # load & build digital twin
│   └── therapy_gen.py     # CRISPR/senolytics/OSKM
├── data/
│   ├── sample_geo.csv     # Yamanaka factors expression
│   └── requirements.txt
├── demos/
│   └── cell_simulator.ipynb
└── lovable/
    └── prompt.txt         # export for lovable.dev UI
```

### Citation
If you use GRA‑CellTwin in your research, please cite the Zenodo DOI above.

---

## Русский

### Что такое GRA‑CellTwin?
GRA‑CellTwin‑Final — это многоуровневый симулятор на основе обобщённого резонансного выравнивания (GRA), создающий точные in silico копии отдельных клеток.
Он объединяет открытые транскриптомные данные (CellxGene, TCGA, GEO) с мультивселенной пеной моделей‑кандидатов.
GRA обнуляет шумы и галлюцинации, гарантируя этичные и объяснимые результаты.

### Ключевые концепции
- **Мультивселенная пена** — популяция микроскопических пузырьков‑моделей, каждый из которых представляет гипотетическое состояние клетки.
- **Критический порог пены** \(\Gamma_{\text{крит}} = \min(\text{плотность пены}, T_c)\)
- **Резонансная частота** (мета‑наблюдатель) \(\omega_{\text{рез}} = \sum \Gamma_{\text{крит}} \cdot R\)
  где \(R\) — пространственная корреляция между пузырьками.
- **GRA‑обнуление** — удаление пузырьков, чей резонанс выходит за пределы критической полосы, что устраняет галлюцинации.
- **Этический фильтр** — блокирует терапии, нарушающие принцип «не навреди».

### Возможности
- Загрузка данных scRNA‑seq (GEO, TCGA BRCA, CellxGene).
- Построение цифровых двойников больных клеток с факторами Яманаки (OSKM).
- Генерация персональной терапии: мишени CRISPR, сенолитики, коктейли репрограммирования.
- Интерактивный Jupyter‑ноутбук с графиками траекторий Plotly.
- Интеграция с LLM (Ollama) и GRA‑постобработка для подавления галлюцинаций.
- Экспортный промпт для двуязычного UI на lovable.dev.

### Установка
```bash
git clone https://github.com/qqewq/GRA-CellTwin-Final.git
cd GRA-CellTwin-Final
pip install -r data/requirements.txt
```

### Быстрый старт
```bash
jupyter notebook demos/cell_simulator.ipynb
```
Вход: breast cancer → Выход: OSKM + senolytics (CRISPR: TP53, MYC).

### Структура репозитория
(см. английскую секцию)

### Цитирование
При использовании GRA‑CellTwin в научных работах ссылайтесь на DOI Zenodo.
