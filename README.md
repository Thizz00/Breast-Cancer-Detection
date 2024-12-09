# Praca-magisterska: **Inteligetny system do diagnozowania Raka Piersi**.

## Zbiór danych

Zbiór danych: **CBIS-DDSM** (Curated Breast Imaging Subset of DDSM). 

Link: https://www.kaggle.com/datasets/awsaf49/cbis-ddsm-breast-cancer-image-dataset.

CBIS-DDSM jest zbiorem danych obrazów medycznych w formacie JPEG. Koncentruje się głównie na obrazowaniu piersi w mammografii. 

**Kluczowe** statystyki zbioru danych:

Liczba badań: **6,775**

Liczba serii: **6,775**

Liczba uczestników: **1,566**

Liczba obrazów: **10,239**

Modalność: **MG (mammografia)**

Rozmiar obrazu: **6 GB w formacie JPEG**

## Instalacja aplikacji 

### Pobranie projektu:

```bash
 git clone https://github.com/Thizz00/Breast-Cancer-Detection.git
```

### Zbudowanie obrazu dockera:

```bash
   docker build -t breast-cancer-detection . 
```

### Uruchomienie kontenera:

```bash
docker run -p 8501:8501 breast-cancer-detection
```

![App Screenshot](/docs/1.png)