# core/utils.py
import os

def get_trace_dir(trace_dir_name):
    # Construct the absolute path to the trace directory
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'traces', trace_dir_name))

def save_trace(context, trace_dir_name, trace_name):
    # Get the absolute path to the trace directory
    trace_dir = get_trace_dir(trace_dir_name)
    
    # Construct the full path to the trace file
    trace_path = os.path.join(trace_dir, trace_name)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(trace_path), exist_ok=True)
    
    # Stop tracing and save the trace to the specified file
    context.tracing.stop(path=trace_path)