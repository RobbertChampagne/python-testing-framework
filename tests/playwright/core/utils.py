# core/utils.py
import os

def get_trace_dir(trace_dir_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'traces', trace_dir_name))

def save_trace(context, trace_dir_name, trace_name):
    trace_dir = get_trace_dir(trace_dir_name)
    trace_path = os.path.join(trace_dir, trace_name)
    os.makedirs(os.path.dirname(trace_path), exist_ok=True)
    context.tracing.stop(path=trace_path)