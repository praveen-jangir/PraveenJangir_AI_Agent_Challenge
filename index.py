import subprocess

# This command starts your streamlit app.
# The --server.headless=true flag is crucial for deployment.
command = "streamlit run app.py --server.port $PORT --server.headless true"

# Run the command and wait for it to complete.
# process.wait() keeps the Vercel function alive as long as Streamlit is running.
process = subprocess.Popen(command, shell=True)
process.wait()
