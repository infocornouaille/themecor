# examples/advanced_demo.py
import os
import subprocess
import time

from themecor import ThemeManager


def main():
    theme_manager = ThemeManager()

    theme_manager.header(
        "Démonstration Avancée", "Gestion de processus avec progression"
    )

    # Exemple de progression manuelle
    progress, task_id = theme_manager.manage_progress(
        None, None, "Initialisation...", 100
    )

    try:
        for i in range(100):
            time.sleep(0.03)
            theme_manager.update_progress(progress, task_id, i + 1, f"Étape {i+1}/100")
    finally:
        theme_manager.stop_progress(progress)

    # Exemple d'exécution de processus avec progression
    # Cet exemple utilise la commande "find" pour rechercher des fichiers
    def update_callback(line, completed):
        # Cette fonction sera appelée pour chaque ligne de sortie du processus
        if line.strip():
            # Incrémenter le progrès à chaque fichier trouvé
            return completed + 1
        return completed

    # Définir le répertoire à analyser
    directory = "."  # Répertoire actuel

    # Créer une nouvelle progression
    progress, task_id = theme_manager.manage_progress(
        None, None, f"Recherche de fichiers dans {directory}", 100
    )

    try:
        # Exécuter la commande (cet exemple fonctionne sous Linux/Mac)
        if os.name == "posix":  # Linux/Mac
            cmd = ["find", directory, "-type", "f"]
        else:  # Windows
            cmd = ["dir", directory, "/s", "/b"]

        theme_manager.run_process_with_progress(
            cmd, progress, task_id, 1, update_callback
        )
    except Exception as e:
        theme_manager.error(f"Erreur lors de l'exécution: {e}")
    finally:
        theme_manager.stop_progress(progress)

    theme_manager.success("Démonstration terminée !")


if __name__ == "__main__":
    main()
