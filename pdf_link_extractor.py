#Autor >> AlfonzCS
import pikepdf # pip3 install pikepdf

def ClownLogo():
    from colorama import init, Fore
    import sys, random, time
    init()
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

        ____  ____  ______   ___       __                __                  __            
       / __ \/ __ \/ ____/  / (_)___  / /__   ___  _  __/ /__________ ______/ /_____  _____
      / /_/ / / / / /_     / / / __ \/ //_/  / _ \| |/_/ __/ ___/ __ `/ ___/ __/ __ \/ ___/
     / ____/ /_/ / __/    / / / / / / ,<    /  __/>  </ /_/ /  / /_/ / /__/ /_/ /_/ / /    
    /_/   /_____/_/      /_/_/_/ /_/_/|_|   \___/_/|_|\__/_/   \__,_/\___/\__/\____/_/     
                                                                                       

      CS! : PDF Link extractor extrae todos los link de los arcivos pdf seleccionados.       
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)

ClownLogo()

try:
	pdf_file = sys.argv[1]
except:
	print('[x] Error')

try:
    file = pdf_file
    # file = "1710.05006.pdf"
    pdf_file = pikepdf.Pdf.open(file)
    urls = []
    # iterate over PDF pages
    for page in pdf_file.pages:
        for annots in page.get("/Annots"):
            uri = annots.get("/A").get("/URI")
            if uri is not None:
                print("[+] URL Found:", uri)
                urls.append(uri)

    print("[*] Total URLs extracted:", len(urls))
except:
	print('[-] PDF no encontrado')
