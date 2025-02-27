# examples/demo.py
import time

from rich.progress import Progress

from themecor import ThemeManager


def main():
    # Initialiser le gestionnaire de thème
    theme_manager = ThemeManager()

    # Afficher un en-tête
    theme_manager.header("Démonstration de ThemeManager", "Exemples d'utilisation")

    # Afficher différents types de messages
    theme_manager.info("Ceci est un message d'information")
    theme_manager.success("Opération réussie !")
    theme_manager.warning("Attention, ceci est un avertissement")
    theme_manager.error("Une erreur s'est produite")
    theme_manager.debug("Information de débogage")

    # Afficher un panneau
    theme_manager.panel(
        "Ce panneau contient des informations importantes pour l'utilisateur.",
        title="Information",
        style="info",
    )

    # Créer et afficher un tableau
    table = theme_manager.table(title="Données", headers=["Nom", "Valeur"])
    table.add_row("Premier", "100")
    table.add_row("Deuxième", "200")
    table.add_row("Troisième", "300")
    theme_manager.console.print(table)

    # Exemple de gestion de progression
    with Progress(console=theme_manager.console) as progress:
        task = progress.add_task("Traitement en cours...", total=100)

        for i in range(100):
            time.sleep(0.05)  # Simuler du travail
            progress.update(task, advance=1)

    # Exemple de confirmation
    if theme_manager.confirm("Voulez-vous continuer ?"):
        theme_manager.success("Continuation confirmée")
    else:
        theme_manager.warning("Opération annulée")

    # Afficher des changements
    changes = [
        ("ancien_fichier.txt", "nouveau_fichier.txt"),
        ("valeur_1", "valeur_2"),
        ("config={debug:False}", "config={debug:True}"),
    ]
    theme_manager.display_changes(changes, title="Modifications effectuées")


if __name__ == "__main__":
    main()
