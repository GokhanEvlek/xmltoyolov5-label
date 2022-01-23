# Function to get the data from XML Annotation
import os
import xml.etree.ElementTree as ET
from tqdm import tqdm
global class_id
def extract_info_from_xml(xml_file):
    root = ET.parse(xml_file).getroot()

    # Initialise the info dict
    info_dict = {}
    info_dict['bboxes'] = []

    # Parse the XML Tree
    for elem in root:
        # Get the file name
        if elem.tag == "filename":
            info_dict['filename'] = elem.text

        # Get the image size
        elif elem.tag == "size":
            image_size = []
            for subelem in elem:
                image_size.append(int(subelem.text))

            info_dict['image_size'] = tuple(image_size)

        # Get details of the bounding box
        elif elem.tag == "object":
            bbox = {}
            for subelem in elem:
                if subelem.tag == "name":
                    bbox["class"] = subelem.text

                elif subelem.tag == "bndbox":
                    for subsubelem in subelem:
                        bbox[subsubelem.tag] = int(subsubelem.text)
            info_dict['bboxes'].append(bbox)

    return info_dict


# Dictionary that maps class names to IDs
class_name_to_id_mapping = {"20": 0,#xmldeki labellarınızı txt de nası görmek istiyorsanız öyle girdi vermelisiniz
                            "30": 1,
                            "dur": 2,
                            "durak": 3,
                            'girisyok':4, 'ilerisag':5, 'ilerisol':6, 'kirmizi':7, 'park':8, 'parkyasak':9, 'sag':10, 'sagadonulmez':11,
                            'sari':12, 'sol':13, 'soladonulmez':14, 'yesil':15}


# Convert the info dict to the required yolo format and write it to disk
def convert_to_yolov5(info_dict):
    print_buffer = []

    # For each bounding box
    for b in info_dict["bboxes"]:
        try:
            class_id = class_name_to_id_mapping[b["class"]]
        except KeyError:
            print("Invalid Class. Must be one from ", class_name_to_id_mapping.keys())

        # Transform the bbox co-ordinates as per the format required by YOLO v5
        b_center_x = (b["xmin"] + b["xmax"]) / 2
        b_center_y = (b["ymin"] + b["ymax"]) / 2
        b_width = (b["xmax"] - b["xmin"])
        b_height = (b["ymax"] - b["ymin"])

        # Normalise the co-ordinates by the dimensions of the image
        image_w, image_h, image_c = info_dict["image_size"]
        b_center_x /= image_w
        b_center_y /= image_h
        b_width /= image_w
        b_height /= image_h

        # Write the bbox details to the file
        print_buffer.append(
            "{} {:.3f} {:.3f} {:.3f} {:.3f}".format(class_id, b_center_x, b_center_y, b_width, b_height))

    

    # Save the annotation to disk

    info_dict["filename"]=info_dict["filename"][:-3]
    info_dict["filename"]=info_dict["filename"]+"txt"
    dosya = open("txt labellarını kaydedeceğiniz yol"+info_dict["filename"], "w")
    uzunluk=len(print_buffer)
    
    i=0

    dosya.write(print_buffer[0]+"\n")#aynı fotoğraf içinde kaç tane labelınız varsa ona göre uzunluk sayısı arttırılabilir
    if uzunluk>=2:
        dosya.write(print_buffer[1] + "\n")
    if uzunluk>=3:
        dosya.write(print_buffer[2] + "\n")
    if uzunluk>=4:
        dosya.write(print_buffer[3] + "\n")
    if uzunluk>=5:
        dosya.write(print_buffer[4] + "\n")

    #print("\n".join(print_buffer), file=open(save_file_name, "w"))
# Get the annotations
annotations = [os.path.join(r'xml labellerının olduğu dosyanın yolu', x) for x in os.listdir(r'xml labellerının olduğu dosyanın yolu') if x[-3:] == "xml"]
annotations.sort()

# Convert and save the annotations
for ann in tqdm(annotations):
    info_dict = extract_info_from_xml(ann)
    convert_to_yolov5(info_dict)





