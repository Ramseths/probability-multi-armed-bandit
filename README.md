# 🎰 Multi-Armed Bandit Algorithm

## 📝 Descripción
Es una implementación del algoritmo de bandidos multi-brazo (Multi-Armed Bandit) utilizando la estrategia **Epsilon-Greedy**. Es una técnica fundamental en el aprendizaje por refuerzo, ideal para situaciones donde un agente debe equilibrar la exploración de nuevas opciones y la explotación de las conocidas.

## 🌟 Características
- **Exploración y Explotación**: Usa Epsilon-Greedy para balancear entre probar nuevos bandidos y seleccionar el mejor conocido. Ideal para entender los conceptos básicos del aprendizaje por refuerzo.

## 🔍 Cómo Funciona
1. **Inicialización**: Se crean tres bandidos con diferentes probabilidades de dar una recompensa.
2. **Ejecución de Episodios**: Durante un número predefinido de episodios, se selecciona un bandido basado en la estrategia Epsilon-Greedy.
3. **Actualización de Valores**: Después de cada episodio, se actualiza el valor esperado de recompensa del bandido seleccionado.
