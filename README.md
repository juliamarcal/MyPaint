# MyPaint

## Visão Geral
MyPaint é um programa gráfico 2D que implementa algoritmos fundamentais de gráficos computacionais para desenhar e transformar formas. O programa inclui funcionalidades para rasterização (desenho de linhas e círculos), transformações geométricas (translação, escala, rotação, reflexão, cisalhamento) e recorte (algoritmos Cohen-Sutherland e Liang-Barsky). Os usuários interagem com o programa através de uma interface gráfica, selecionando e modificando formas dinamicamente.

## Funcionalidades
### Transformações Geométricas
- **Translação**: Move objetos ao longo dos eixos X e Y.
- **Escala**: Redimensiona objetos ao longo dos eixos X e Y.
- **Rotação**: Roda objetos por um ângulo especificado em torno de seu centro.
- **Reflexão**: Reflete objetos sobre o eixo X ou Y.
- **Cisalhamento**: Aplica a transformação de cisalhamento ao longo dos eixos X ou Y.

### Rasterização (Desenho de Linhas e Círculos)
- **Algoritmo DDA**: Desenha linhas usando o método Digital Differential Analyzer.
- **Algoritmo de Bresenham para Linhas**: Rasterização eficiente de linhas com cálculos inteiros.
- **Algoritmo de Bresenham para Círculos**: Rasterização de círculos usando operações baseadas em inteiros.

### Recorte (Corte de Formas Baseado em Região)
- **Algoritmo Cohen-Sutherland**: Recorte eficiente de linhas contra uma região retangular.
- **Liang-Barsky Algorithm**: Usa equações parametrizadas para recorte de linhas de forma otimizada.

## Requisitos
Certifique-se de que você tem as dependências necessárias antes de rodar o programa:
- Python 3.x
- Módulos necessários: `math`, `tkinter` (for GUI), `numpy`

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/yourusername/mypaint.git
   ```
2. Navegue até a pasta do projeto:
   ```bash
   cd mypaint
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
Execute o programa com:
```bash
python src/main.py
```

### Interação
- O usuário pode desenhar linhas, círculos e polígonos clicando na tela.
- O sistema de menus permite a seleção de transformações e operações de recorte.
- A tela é atualizada dinamicamente para refletir as operações aplicadas.

## File Structure
```
mypaint/
│── src/
│   │── main.py                  # Ponto de entrada do programa
│   │── transformations.py       # Implementação da lógica das transformações
│   │── rasterization.py         # Algoritmos de desenho de linhas e círculos
│   │── clipping.py              # Implementação dos algoritmos de recorte
│   │── menu_utils.py            # Funções utilitárias relacionadas ao menu
│   │── canvas_utils.py          # Funções de gerenciamento da tela de desenho
│── README.md                    # Documentação
```
