from py4j.java_gateway import JavaGateway, CallbackServerParameters
import subprocess
import os

class VendorAnalysisEntryPoint:
    def run_analysis(self):
        try:
            # Run the main Python analysis script
            subprocess.run(["python", "aiims_vendor_analysis.py"], check=True)
            
            # Optionally, start Flask app
            subprocess.Popen(["python", "app.py"])
            
            return "AIIMS Vendor Analysis started and Flask server launched."
        except Exception as e:
            return f"Error: {str(e)}"

# Start the Py4J gateway server
gateway = JavaGateway(
    callback_server_parameters=CallbackServerParameters()
)
gateway.entry_point = VendorAnalysisEntryPoint()
print("Python Gateway Started")



