#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

mod dataset;

use std::path::PathBuf;

use dataset::Dataset;

#[tauri::command]
fn load_dataset(dataset_path: PathBuf) -> Dataset {
    Dataset::from_path(dataset_path)
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![load_dataset])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}