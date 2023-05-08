import os
import xml.etree.ElementTree as ET


def allure_environment_writer(environment_values_set, custom_results_path=None):
    environment = ET.Element("environment")
    for k, v in environment_values_set.items():
        parameter = ET.SubElement(environment, "parameter")
        key = ET.SubElement(parameter, "key")
        value = ET.SubElement(parameter, "value")
        key.text = k
        value.text = v
    if custom_results_path is None:
        allure_results_dir = os.path.join(os.getcwd(), "target", "allure_results")
        if not os.path.exists(allure_results_dir):
            os.makedirs(allure_results_dir)
        output_path = os.path.join(allure_results_dir, "environment.xml")
    else:
        if not os.path.exists(custom_results_path):
            os.makedirs(custom_results_path)
        output_path = os.path.join(custom_results_path, "environment.xml")
    tree = ET.ElementTree(environment)
    tree.write(output_path)
    print("Allure environment data saved.")
