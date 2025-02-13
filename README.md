# pythongames_simonsays

# 🎮 Simon Says | Simon Dice

[English](#english) | [Español](#español)

# English

## 📝 Description
A memory game based on the classic Simon Says, with two different implementations:
1. Console version with emojis and time limits
2. Graphical version with interactive buttons and difficulty levels

## 🎯 Features

### Console Version (simon_console.py)
- Emoji-based color sequence
- Time limit for responses
- Keyboard input
- Progress tracking up to 10 sequences
- Color codes: B(Blue 🔵), G(Green 🟢), R(Red 🔴), Y(Yellow 🟡), P(Purple 🟣)

### GUI Version (simon_gui.py)
- Interactive pentagon-shaped buttons
- Three difficulty levels (Easy, Medium, Hard)
- High score tracking
- Click counter
- Visual feedback with color transitions
- Continue button for next sequence

## 📋 Requirements
- Python 3.x
- Required libraries:
  - pyautogui (Console version)
  - tkinter (GUI version)

## 💻 Installation

1. Clone this repository:
```bash
git clone <repository-url>
```

2. Install required dependencies:
```bash
pip install pyautogui
```

3. Run either version:
```bash
# For console version
python simon_console.py

# For GUI version
python simon_gui.py
```

## 🎮 How to Play

### Console Version
1. Watch the sequence of colors shown
2. Type the sequence using letters (B, G, R, Y, P)
3. Complete within the time limit
4. Try to reach 10 sequences

### GUI Version
1. Select difficulty level
2. Click "Start Game"
3. Watch the sequence
4. Click the colored pentagons in the same order
5. Click "Continue" for next sequence
6. Try to achieve the highest score

## 🎯 Difficulty Levels (GUI Version)
- Easy: 1.5x normal display time
- Medium: Normal display time
- Hard: 0.5x normal display time

---

# Español

## 📝 Descripción
Un juego de memoria basado en el clásico Simon Dice, con dos implementaciones diferentes:
1. Versión de consola con emojis y límites de tiempo
2. Versión gráfica con botones interactivos y niveles de dificultad

## 🎯 Características

### Versión Consola (simon_console.py)
- Secuencia de colores basada en emojis
- Límite de tiempo para respuestas
- Entrada por teclado
- Seguimiento de progreso hasta 10 secuencias
- Códigos de color: B(Azul 🔵), G(Verde 🟢), R(Rojo 🔴), Y(Amarillo 🟡), P(Morado 🟣)

### Versión GUI (simon_gui.py)
- Botones interactivos en forma de pentágono
- Tres niveles de dificultad (Fácil, Medio, Difícil)
- Registro de puntuación más alta
- Contador de clicks
- Retroalimentación visual con transiciones de color
- Botón de continuar para siguiente secuencia

## 🛠️ Technical Details / Detalles Técnicos

### Console Version / Versión Consola
```python
# Color and emoji mappings
color_list = ["B", "G", "R", "Y", "P"]
emoji_list = ["🔵​", "🟢", "🔴", "🟡", "🟣", "❌"]

# Time limit for input
time_limit = 5  # seconds
```

### GUI Version / Versión GUI
```python
# Difficulty settings
difficulties = {
    "Easy": 1.5,    # 150% of base time
    "Medium": 1.0,  # 100% of base time
    "Hard": 0.5     # 50% of base time
}

# Colors configuration
colors = ["blue", "green", "red", "yellow", "purple"]
light_colors = ["light blue", "light green", "pink", "khaki", "plum"]
```

## ✨ Possible Improvements / Posibles Mejoras
- Add sound effects / Añadir efectos de sonido
- Implement multiplayer mode / Implementar modo multijugador
- Add animations / Agregar animaciones
- Include different patterns / Incluir patrones diferentes
- Save high scores to file / Guardar puntuaciones en archivo

## 🔧 Project Structure / Estructura del Proyecto
```
simon-says/
├── simon_console.py  # Console version
├── simon_gui.py      # GUI version
└── README.md         # Documentation
```

## 🤝 Contributing / Contribuir
1. Fork the project / Haz un Fork del proyecto
2. Create your feature branch / Crea una rama para tu función
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes / Haz commit de tus cambios
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch / Push a la rama
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request / Abre un Pull Request

## 📜 License / Licencia
[Include license type / Incluir tipo de licencia]

## 📞 Contact / Contacto
[Include contact information / Incluir información de contacto]
