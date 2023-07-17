import streamlit as st
import file
import graph

def main():
    file.handle_pdf()
    graph.handle_graph()
    
if __name__ == "__main__":
    main()
