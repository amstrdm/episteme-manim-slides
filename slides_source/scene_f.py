from manim import *

# Annahme: Eine Farbklasse ist definiert. Falls nicht, werden hier Standardfarben verwendet.
class PresentationColors:
    BACKGROUND = BLACK
    TEXT_PRIMARY = WHITE
    TEXT_SECONDARY = LIGHT_GRAY
    ACCENT_MAIN = BLUE_C
    ACCENT_HIGHLIGHT = YELLOW_C

config.background_color = PresentationColors.BACKGROUND
config.frame_height = 9
config.frame_width = 16

def FazitSlide(self):
    # Hauptüberschrift
    title = Text("Fazit & Ausblick", font_size=64).to_edge(UP, buff=0.8)
    self.play(Write(title))
    self.next_slide()

    # --- Zusammenfassung ---
    summary_title = Text("Zusammenfassung der Ergebnisse", font_size=40, color=PresentationColors.ACCENT_MAIN)
    summary_title.next_to(title, DOWN, buff=0.7, aligned_edge=LEFT).shift(LEFT * 2)

    summary_points_text = [
        "- Voll funktionsfähige Webanwendung zur Recherche-Automatisierung",
        "- Eliminierung von Redundanz durch semantische Duplikatfilterung",
        "- Schnelle, fehlertolerante Suche mittels Trigramm-Indizierung",
        "- Intuitive Darstellung komplexer Daten im Frontend"
    ]

    summary_points = VGroup(*[
        Text(point, font_size=32, color=PresentationColors.TEXT_PRIMARY) 
        for point in summary_points_text
    ]).arrange(DOWN, buff=0.3, aligned_edge=LEFT).shift(LEFT * 1)
    summary_points.next_to(summary_title, DOWN, buff=0.4, aligned_edge=LEFT)
    summary_points.set_width(config.frame_width * 0.7) # Sicherstellen, dass es passt

    self.play(FadeIn(summary_title, shift=RIGHT))
    self.next_slide()

    # Punkte nacheinander animieren
    for point in summary_points:
        self.play(Write(point), run_time=1.2)
        self.next_slide()
    
    # --- Ausblick ---
    outlook_title = Text("Möglicher Ausblick", font_size=40, color=PresentationColors.ACCENT_HIGHLIGHT)
    outlook_title.next_to(summary_points, DOWN, buff=0.8, aligned_edge=LEFT).align_to(summary_title, LEFT)

    outlook_points_text = [
        "- Erweiterung um zusätzliche Datenquellen (z.B. Nachrichten-APIs)",
        "- Performance-Optimierung des Backends (z.B. durch Golang)",
        "- Detailliertere Analyse der Autoren-Performance"
    ]

    outlook_points = VGroup(*[
        Text(point, font_size=32, slant=ITALIC, color=PresentationColors.TEXT_SECONDARY)
        for point in outlook_points_text
    ]).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
    outlook_points.next_to(outlook_title, DOWN, buff=0.4, aligned_edge=LEFT)
    outlook_points.set_width(config.frame_width * 0.7)

    self.play(FadeIn(outlook_title, shift=RIGHT))
    self.next_slide()
    for point in outlook_points:
        self.play(FadeIn(point, shift=UP*0.2), run_time=0.8)
        self.next_slide()
    
    self.wipe(self.mobjects, direction=UP)
