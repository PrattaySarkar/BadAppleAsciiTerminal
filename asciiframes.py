from ascii_magic import from_image
import os


# Function to convert an image to ASCII art and save it to a text file
def convert_image_to_ascii(input_image_path, output_text_path):
    ascii_art = from_image(input_image_path)
    with open(output_text_path, "w") as text_file:
        text_file.write(str(ascii_art))


# Function to convert all JPGs in a folder to ASCII art and save them in another folder
def batch_convert_to_ascii(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            input_image_path = os.path.join(input_folder, filename)
            output_text_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")
            convert_image_to_ascii(input_image_path, output_text_path)


if __name__ == "__main__":
    input_folder = "input_images"  # Replace with the path to your input folder containing JPGs
    output_folder = "output_folder"  # Replace with the path to your output folder
    batch_convert_to_ascii(input_folder, output_folder)
