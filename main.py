import argparse
import analysis
import scan
import report





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scans the target send it to ai to write reports and tips for enhancing the security of the target")
    parser.add_argument("--target","-t",type=str,help="Ip adress",required=True)
    parser.add_argument("--wordlist","-w",type=str,help="Custom wordlist",default="/usr/share/seclists/common.txt")
    args = parser.parse_args()
    config = analysis.load_config("config.json")


    print(f"[i] Target locked {args.target}")
    print(f"Word list for gobuster: {args.wordlist}\n")

    print("Starting nmap scan please wait ....")
    nmap = scan.run_nmap(args.target)
    print("Done!\n")
    
    

    print("Starting gobuster scan please wait ....")
    gobuster = scan.run_gobuster(args.target,args.wordlist)
    print("Done!\n")

    print("Starting nikto scan please wait ....")
    nikto = scan.run_nikto(args.target)
    print("Done!\n")

    print("Starting virus total scan please wait ....")
    virustotal = analysis.check_virustotal(args.target,config["VIRUSTOTAL_API_KEY"])
    print("Done!\n")


    print("Starting abuseipdb scan please wait ....")
    abuseipdb = analysis.check_abuseipdb(args.target,config["ABUSEDB_API_KEY"])
    print("Done!\n")

    print("Generating master report ...")
    report.gen_report(args.target,nmap,gobuster,nikto,virustotal,abuseipdb)
    print("Done\n")

    with open("report.txt","r") as file:
        master_report = file.read()

    print("Sending to Gemini for analysis please wait ....")
    gemini_report = analysis.ask_gemini(master_report,config["GEMINI_API_KEY"])
    print("Done!\n")

    print("Report saved in report.txt")
    print("Gemini report saved in gemini_report.txt")

    with open("gemini_report.txt","w") as file:
        file.write(gemini_report)


