import subprocess 
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest = "interface", help ="interface para cambiar Direccion MAC") 
    parser.add_option("-m", "--mac", dest = "new_mac", help ="Nueva Direccion MAC") 
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-]Por favor indicar una interfaz, usa --help para mas informacion")
    elif not options.new_mac:
        parser.error("[-]Por favor indicar una direccion MAC, usa --help para mas informacion")
    return options 

def change_mac(interface, new_mac):

    print("[+] Cambiando Direccion MAC para " + interface + " a " + new_mac )

    subprocess.call(["ifconfig", interface, "down"] ) 
    subprocess.call(["ifconfig", interface, "hw" , "ether", new_mac] )
    subprocess.call(["ifconfig", interface, "up"] )

def get_current_mac(interface):
  ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
  a = ifconfig_result.decode("UTF-8")
  mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", a)

  if mac_address_search_result:
        return mac_address_search_result.group(0)
  else:
    print("[-] No puedimos leer direccion MAC")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("current MAC = " + str(current_mac))

change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] direccion MAC SI se cambio correctamente a " + current_mac)
else:
    print("[-] direccion MAC NO se pudo cambiar correctamente") 