# Henry González Alguera · Developer Portfolio

Sitio personal profesional para presentar proyectos de **C#/.NET**, **Azure**, **Python/Data Analytics** y **Java/Spring Boot**. Versión inicial creada para la Fase 7 del portafolio de GitHub/LinkedIn.

## Características

- Sitio **responsive** en HTML, CSS y JavaScript sin frameworks ni necesidad de compilar.
- Interfaz en **inglés y español** (selector ES/EN).
- Filtros de proyectos por .NET, Python/Data y Java.
- Imágenes reales cuando están disponibles y diagramas ilustrativos claramente etiquetados.
- Metadatos SEO, Open Graph, accesibilidad básica y diseño adaptativo.
- Enlaces públicos a los cuatro repositorios, demos Azure, GitHub y LinkedIn.
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

## Publicar gratis con GitHub Pages (sitio personal)

1. En GitHub, haz clic en **New repository** (`https://github.com/new`).
2. Pon exactamente el nombre **`HenryGonzalezAlguera.github.io`** (mismas mayúsculas del usuario, no es obligatorio pero ayuda a identificarlo). Selecciona **Public**. Crea el repositorio **vacío** (sin README inicial, gitignore ni licencia). **Este repositorio aún no existe y debe crearse desde tu cuenta.**
3. Descomprime el ZIP y abre PowerShell dentro de la carpeta `henry-dev-portfolio`.
4. Ejecuta:

   ```powershell
   git init
   git branch -M main
   git add .
   git commit -m "feat: publish personal developer portfolio v1"
   git remote add origin https://github.com/HenryGonzalezAlguera/HenryGonzalezAlguera.github.io.git
   git push -u origin main
   ```

5. Abre el repositorio recién creado → **Settings** → **Pages** → **Build and deployment** → **Source: Deploy from a branch** → **Branch: `main` / `(root)`** → **Save**.
6. GitHub Pages debería ofrecer el sitio en **`https://henrygonzalezalguera.github.io/`** una vez que termine el despliegue. No consideres ese enlace activo hasta comprobarlo en tu navegador.
7. Cuando esté publicado, agrega el enlace en tu **GitHub Profile**, tu sección **Destacados de LinkedIn** y tus CV.

### Alternativa sin comandos

Desde el repositorio nuevo usa **Add file → Upload files** y arrastra `index.html`, la carpeta `assets` y `.nojekyll` desde la carpeta descomprimida, luego **Commit changes**; confirma que `index.html` quede en la raíz (no dentro de una subcarpeta). Después configura GitHub Pages siguiendo el paso 5.

## Pendientes opcionales de Fase 7.1

- Añadir un **CV final en PDF** cuando lo preparemos en la fase de CV, y habilitar el botón de descarga.
- Incorporar capturas nuevas y anonimizadas de Restaurante.
- Sustituir las imágenes remotas de StockFlow/Data Quality por archivos locales para una página completamente independiente.
- Añadir favicon y Open Graph definitivos si cambia el dominio.
- Revisar el texto de trayectoria profesional con el CV final antes de dar el sitio por definitivo.

**Notas de exactitud**: el grado está **pendiente** de TCU; el sitio no afirma tener experiencia laboral remunerada como desarrollador. Las demos Azure son de portafolio y pueden estar temporalmente inactivas. Data Quality utiliza datos sintéticos. Restaurante es una demo local.