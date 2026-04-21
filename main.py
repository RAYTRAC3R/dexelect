import argparse
from data.loader import build_all_data_structures
from ui.cli import ui_loop

def main():
    parser = argparse.ArgumentParser(description="TeamGen")
    parser.add_argument("--ui", choices=["cli", "gui"], default="cli")
    args = parser.parse_args()

    all_pools, all_pokemon, config_data, meta_data, mappings, global_settings = build_all_data_structures()

    if args.ui == "gui":
        from ui.gui import TeamGenApp
        app = TeamGenApp(all_pools, all_pokemon, config_data, meta_data, mappings, global_settings)
        app.mainloop()
    else:
        ui_loop(all_pools, all_pokemon, config_data, meta_data, mappings, global_settings)

if __name__ == "__main__":
    main()
