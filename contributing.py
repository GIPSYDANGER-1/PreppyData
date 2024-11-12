class ContributingGuidelines:
    def __init__(self):
        self.code_of_conduct = {
            "respect": "Treat all contributors with respect and courtesy",
            "inclusivity": "Foster an open community where everyone can participate",
            "constructive": "Provide constructive feedback"
        }
        
    def how_to_contribute(self):
        contribution_types = {
            "code_contributions": [
                "Fix bugs",
                "Implement new features", 
                "Improve documentation",
                "Write tests"
            ],
            "non_code_contributions": [
                "Report issues",
                "Answer questions",
                "Documentation",
                "Community support"
            ]
        }
        return contribution_types
        
    def pull_request_process(self):
        steps = [
            "1. Fork the repository",
            "2. Create development branch",
            "3. Make changes and test",
            "4. Write commit messages",
            "5. Create PR",
            "6. Address review feedback"
        ]
        return steps
        
    def code_style(self):
        style_guide = {
            "formatting": "Use black and ruff",
            "documentation": "Follow Google style guide",
            "testing": "Write unit tests with pytest",
            "commits": "Write clear commit messages"
        }
        return style_guide

def main():
    guide = ContributingGuidelines()
    print("Welcome to the Contributing Guidelines!")
    print("\nCode of Conduct:")
    for key, value in guide.code_of_conduct.items():
        print(f"- {key.title()}: {value}")
        
    print("\nWays to Contribute:")
    for type, methods in guide.how_to_contribute().items():
        print(f"\n{type.replace('_', ' ').title()}:")
        for method in methods:
            print(f"- {method}")
            
    print("\nPR Process:")
    for step in guide.pull_request_process():
        print(step)
        
    print("\nCode Style:")
    for key, value in guide.code_style().items():
        print(f"- {key.title()}: {value}")

if __name__ == "__main__":
    main() 