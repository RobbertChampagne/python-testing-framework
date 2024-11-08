import os
from pytest_html import extras as html

def pytest_html_results_summary(prefix, summary, postfix):
    
    environment = os.getenv("ENVIRONMENT")
    
    # Create a table with environment information using raw HTML
    table_html = """
     <style>
        .summary-table {{
            width: 20%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 11px;
            text-align: left;
        }}
        .summary-table th, .summary-table td {{
            padding: 12px 15px;
            border: 1px solid #ddd;
        }}
        .summary-table th {{
            background-color: #f2f2f2;
        }}
        
    </style>
    <table class="summary-table">
        <tr>
            <th>Key</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Environment</td>
            <td>{}</td>
        </tr>
    </table>
    """.format(environment)
    
    # Add custom content to prefix
    prefix.extend([("Test Execution Summary")])
    
    # Add the table to the summary
    summary.extend([table_html])
    
    # Add custom content to postfix
    postfix.extend([("End of Summary")])

