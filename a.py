import os
import csv
import pydicom

def read_dicom_files(directory):
  """Reads DICOM files from the specified directory and returns a list of DICOM objects."""
  dicom_files = []
  for file in os.listdir(directory):
    if file.endswith(".dcm"):
      dicom_file = pydicom.dcmread(os.path.join(directory, file))
      dicom_files.append(dicom_file)
  return dicom_files

def write_csv(dicom_files, output_file):
  """Writes the specified DICOM files to a CSV file."""
  with open(output_file, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Manufacturer", "Acquisition Date", "Model Name", "Slice Thickness", "X Ray Tube Current"])
    for dicom_file in dicom_files:
      csvwriter.writerow([
          dicom_file.Manufacturer,
          dicom_file.AcquisitionDate,
          dicom_file.ModelName,
          dicom_file.SliceThickness,
          dicom_file.XRayTubeCurrent
      ])

def main():
  directory = "/home/amity/Desktop/ai.py"
  output_file = "output.csv"

  dicom_files = read_dicom_files(directory)
  write_csv(dicom_files, output_file)

if __name__ == "__main__":
  main()

