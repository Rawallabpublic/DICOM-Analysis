import os
import pydicom
import csv

def read_dicom_files(directory):
    dicom_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".dcm"):
            dicom_files.append(os.path.join(directory, filename))
    return dicom_files

def process_dicom_files(dicom_files):
    rows = []
    for file_path in dicom_files:
        ds = pydicom.dcmread(file_path)
        manufacturer = ds.get("Manufacturer", "N/A")
        acquisition_date = ds.get("AcquisitionDate", "N/A")
        model_name = ds.get("ManufacturerModelName", "N/A")
        slice_thickness = ds.get("SliceThickness", "N/A")
        xray_tube_current = ds.get("XRayTubeCurrent", "N/A")
        rows.append([manufacturer, acquisition_date, model_name, slice_thickness, xray_tube_current])
    return rows

def write_csv(output_file, rows):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Manufacturer', 'Acquisition Date', 'Model Name', 'Slice Thickness', 'X-ray Tube Current'])
        writer.writerows(rows)

# Directory where the DICOM files are stored
directory = "/home/amity/Desktop/ai.py"

# Output CSV file path
output_file = "output2.csv"

# Read DICOM files from the directory
dicom_files = read_dicom_files(directory)

# Process DICOM files and extract relevant information
rows = process_dicom_files(dicom_files)

# Write the extracted information to a CSV file
write_csv(output_file, rows)

print(f"CSV file '{output_file}' created successfully.")

