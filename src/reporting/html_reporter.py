from pathlib import Path 

def generate_html_report(results: dict, output_path: str):
    """
    Generate a basic HTML report for data quality results.
    """

    html_content = f"""
    <html>
    <head>
        <title> Data Quality Report </title>
        <style>
            body {{font-family: Arial; margin: 20px; }}
            h1 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 50%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
            th {{ background-color: #f4f4f4; }}
        </style>
    </head>
    <body>
        <h1>Data Quality Report</h1>
        <h2>Dataset: {results["filename"]}</h2>

        <table>
            <tr><th>Metric</th><th>Value</th></tr>
            <tr><td>Row Count</td><td>{results["row_count"]}</td></tr>
            <tr><td>Column Count</td><td>{results["col_couunt"]}</td></tr>
            <tr><td>Quality Score</td><td>{results["quality_score"]}</td></tr>
            <tr><td>Null Rate</td><td>{results["null_rate"]}</td></tr>
            <tr><td>Outlier Count</td><td>{results["outlier_count"]}</td></tr>
            <tr><td>Run Timestamp</td><td>{results["run_at"]}</td></tr>
        </table>

    </body>
    </html>
    """

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)