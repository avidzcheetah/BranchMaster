import os
from src.analyzer import AutoPRAnalyzer

def main():
     print("""
       ____     ____        _      _   _      ____   _   _        __  __      _      ____     _____  U _____ u   ____     
    U | __")uU |  _"\ u U  /"\  u | \ |"|  U /"___| |'| |'|     U|' \/ '|uU  /"\  u / __"| u |_ " _| \| ___"|/U |  _"\ u  
     \|  _ \/ \| |_) |/  \/ _ \/ <|  \| |> \| | u  /| |_| |\    \| |\/| |/ \/ _ \/ <\___ \/    | |    |  _|"   \| |_) |/  
      | |_) |  |  _ <    / ___ \ U| |\  |u  | |/__ U|  _  |u     | |  | |  / ___ \  u___) |   /| |\   | |___    |  _ <    
      |____/   |_| \_\  /_/   \_\ |_| \_|    \____| |_| |_|      |_|  |_| /_/   \_\ |____/>> u |_|U   |_____|   |_| \_\   
     _|| \\_   //   \\_  \\    >> ||   \\,-._// \\  //   \\     <<,-,,-.   \\    >>  )(  (__)_// \\_  <<   >>   //   \\_  
    (__) (__) (__)  (__)(__)  (__)(_")  (_/(__)(__)(_") ("_)     (./  \.) (__)  (__)(__)    (__) (__)(__) (__) (__)  (__) 
                                                                           __            ___ _   _________  ____  
                                                                          / /  __ __    / _ | | / /  _/ _ \/_  /  
                                                                         / _ \/ // /   / __ | |/ // // // / / /_  
                                                                        /_.__/\_, /   /_/ |_|___/___/____/ /___/  
                                                                            /___/  
           https://github.com/avidzcheetah 

""")
    token = os.getenv('GITHUB_TOKEN') or input("Enter your GitHub token: ")
    repo_name = input("Enter repository name (owner/repo): ")

    analyzer = AutoPRAnalyzer(token, repo_name)
    
    print(f"Starting analysis of repository: {repo_name}")
    print(f"Default branch: {analyzer.default_branch}")
    
    analyses = analyzer.analyze_all_branches_and_forks()
    
    print("\nAnalysis Results:")
    for analysis in analyses:
        print(f"\n{'Fork' if analysis.is_fork else 'Branch'}: {analysis.branch_name}")
        print(f"Impact Score: {analysis.impact_score:.2f}")
        print("Suggested Improvements:")
        for improvement in analysis.improvements:
            print(f"- {improvement}")

if __name__ == "__main__":
    main()
