import argparse
import scan
import report



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scans the target send it to ai to write reports and tips for enhancing the security of the target")
    parser.add_argument("--target","-t",type=str,help="Ip adress",required=True)
    parser.add_argument("--wordlist","-w",type=str,help="Custom wordlist",default="/usr/share/seclists/common.txt")
    args = parser.parse_args()



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

    report.gen_report(args.target,nmap,gobuster,nikto)
