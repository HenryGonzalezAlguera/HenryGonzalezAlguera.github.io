# Henry González Alguera · Developer Portfolio

Sitio personal profesional para presentar proyectos de **C#/.NET**, **Azure**, **Python/Data Analytics** y **Java/Spring Boot**. Versión inicial creada para la Fase 7 del portafolio de GitHub/LinkedIn.

## Características

- Sitio **responsive** en HTML, CSS y JavaScript sin frameworks ni necesidad de compilar.
- Interfaz en **inglés y español** (selector ES/EN).
- Filtros de proyectos por .NET, Python/Data y Java.
- Imágenes reales cuando están disponibles y diagramas ilustrativos claramente etiquetados.
- Metadatos SEO, Open Graph, accesibilidad básica y diseño adaptativo.
- Enlaces públicos a los cuatro repositorios, demos Azure, GitHub y LinkedIn.
- CV público descargable en **inglés y español** desde la portada y el pie del sitio; el botón cambia con ES/EN. Las versiones públicas **no muestran teléfono ni correo personal**.
- No recopila información personal ni envía datos a terceros mediante formularios. Las tipografías de Google Fonts y las capturas servidas desde GitHub son solicitudes externas que puedes quitar si necesitas un sitio 100 % autocontenido.

## Archivos

```text
index.html                   # Una sola página con hero, proyectos, aptitudes, trayectoria y contacto
assets/site.css              # Diseño responsive
assets/site.js               # Idiomas, filtros, menú móvil
assets/suwogym-admin.webp    # Captura real de SUWÓ GYM; recortada sin datos de pago
assets/stockflow-fallback.svg# Imagen de respaldo ilustrativa
assets/dataquality-fallback.svg
assets/restaurante-architecture.svg
assets/favicon.svg
assets/og-cover.png          # Tarjeta de vista previa social
.nojekyll                   # Publicación estática en GitHub Pages
```

StockFlow y Data Quality usan **capturas originales** servidas desde `raw.githubusercontent.com` con ilustraciones de respaldo por si no cargan. SUWÓ GYM utiliza una captura proporcionada directamente por el autor. Restaurante solo usa una **ilustración de arquitectura**, no un falso screenshot.

## Probar en tu computadora

1. Descarga y descomprime el ZIP en una carpeta.
2. Haz doble clic en `index.html` para abrir el sitio. Para un comportamiento similar a producción, desde la carpeta ejecuta:

   ```powershell
   py -m http.server 5500
   ```

3. Visita `http://localhost:5500/`.
4. Revisa escritorio y teléfono, botones ES/EN y filtros de proyecto.

## Sitio publicado en GitHub Pages

- **Sitio:** https://henrygonzalezalguera.github.io/
- **Repositorio público:** https://github.com/HenryGonzalezAlguera/HenryGonzalezAlguera.github.io
- **Rama de publicación:** `main`, raíz `/`.
- **Comprobación:** [GitHub Actions — Portfolio Static Checks](https://github.com/HenryGonzalezAlguera/HenryGonzalezAlguera.github.io/actions/workflows/portfolio-ci.yml).
- El despliegue de GitHub Pages se ejecuta automáticamente con los cambios en `main`. Puede tardar unos minutos en reflejar actualizaciones.

### Actualizar la página

Edita `index.html` y los archivos de `assets/` y registra un commit en `main` (directamente desde GitHub o mediante git local). Las pruebas comprueban estructura, enlaces internos y sintaxis del JavaScript. Confirma el resultado en el navegador desde escritorio y móvil.

### Prueba local

```powershell
py -m http.server 5500
```

Abre http://localhost:5500/ desde la carpeta que contiene `index.html`. No se requiere instalar .NET, Java, Python libraries ni base de datos para usar este portafolio estático.

## Pendientes opcionales de Fase 7.1

- Personalizar el CV publicado por vacante; las versiones específicas para postulaciones se comparten de forma privada y no están alojadas aquí.
- Incorporar capturas nuevas y anonimizadas de Restaurante.
- Sustituir las imágenes remotas de StockFlow/Data Quality por archivos locales para una página completamente independiente.
- Añadir favicon y Open Graph definitivos si cambia el dominio.
- Revisar el texto de trayectoria profesional con el CV final antes de dar el sitio por definitivo.

**Notas de exactitud**: el grado está **pendiente** de TCU; el sitio no afirma tener experiencia laboral remunerada como desarrollador. Las demos Azure son de portafolio y pueden estar temporalmente inactivas. Data Quality utiliza datos sintéticos. Restaurante es una demo local.