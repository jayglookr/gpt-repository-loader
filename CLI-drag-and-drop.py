import os
import subprocess

output_directory = os.path.expanduser("~/git-as-txt/")

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)
print(f"Output directory is set to: {output_directory}")

def process_repository(repo_path):
    # Extract the repository name
    repo_name = os.path.basename(repo_path)
    output_file_path = os.path.join(output_directory, repo_name + ".txt")

    # Handle potential naming conflicts
    counter = 1
    while os.path.exists(output_file_path):
        # Append a counter to the filename
        output_file_path = os.path.join(output_directory, f"{repo_name}({counter}).txt")
        counter += 1

    # Run gpt-repository-loader on the repository
    print(f"Processing repository: {repo_path}")
    subprocess.run(["python", "gpt_repository_loader.py", repo_path, "-o", output_file_path])

    print(f"Repository processed and saved to {output_file_path}")

print("Hi, welcome! Pass me a Git repository to process:")

while True:
    try:
        # Prompt for the repository path
        repo_path = input("Repository path: ")

        # Check if the user wants to exit
        if repo_path.lower() == "exit":
            break

        # Check if the repository exists
        if not os.path.isdir(repo_path):
            print(f"Error: {repo_path} is not a valid directory path.")
            continue

        # Process the repository
        process_repository(repo_path)

        print("Pass another repository or type 'exit' to quit.")

    except Exception as e:
        print("Error:", str(e))

print("Exiting. Goodbye!")
