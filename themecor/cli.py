# themecor/cli.py

from themecor import ThemeManager

# Initialize ThemeManager
theme_manager = ThemeManager()

# Initialize Typer app for CLI commands
typer = theme_manager.typer
app = typer.Typer()


@app.command()
def demo():
    """Exécute une démonstration des fonctionnalités de ThemeManager."""
    theme_manager.header("Démonstration CLI de ThemeManager")
    theme_manager.info("Affichage des différents types de messages")
    theme_manager.success("Opération réussie")
    theme_manager.warning("Avertissement")
    theme_manager.error("Erreur")
    theme_manager.debug("Débogage")

    theme_manager.panel("Exemple de panneau", title="Information", style="info")

    # Tableau d'exemple
    table = theme_manager.table(title="Exemple de tableau", headers=["Clé", "Valeur"])
    table.add_row("Nom", "ThemeManager")
    table.add_row("Version", "0.1.0")
    table.add_row("Description", "Gestionnaire de thème pour CLI")
    theme_manager.console.print(table)


@app.command()
def config(
    show_default: bool = typer.Option(
        False, "--show-default", "-d", help="Afficher la configuration par défaut"
    )
):
    """Affiche la configuration actuelle du thème."""
    if show_default:
        theme_manager.header("Configuration par défaut")
        for key, value in ThemeManager.DEFAULT_THEME.items():
            theme_manager.console.print(f"[key]{key}[/key]: [value]{value}[/value]")
    else:
        theme_manager.header("Configuration personnalisée")
        theme_manager.panel(
            "Utilisez l'option --show-default pour voir la configuration par défaut",
            style="info",
        )


if __name__ == "__main__":
    app()
