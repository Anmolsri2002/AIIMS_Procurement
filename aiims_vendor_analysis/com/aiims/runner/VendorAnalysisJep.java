package com.aiims.runner;
import jep.Interpreter;
import jep.SharedInterpreter;

public class VendorAnalysisJep {
    public static void main(String[] args) {
        try (Interpreter py = new SharedInterpreter()) {
            py.exec("import sys");
            py.exec("sys.path.append('python')");  // make sure your Python folder is in path

            // Run analysis
            py.exec("import aiims_vendor_analysis");
            py.exec("aiims_vendor_analysis.main()");

            // Optional: start Flask app if you want
            // py.exec("import app");
            // py.exec("app.start_flask()");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
