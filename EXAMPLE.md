# Example: Terminal RAG Agent with MCPM

This query plan demonstrates how to build a working RAG agent using MCPM and Claude Code. Copy these prompts in sequence to go from zero to a functioning terminal RAG application.

## Prerequisites
- Claude Desktop with MCPM configured
- A folder with documents to index (e.g., `~/Documents/knowledge-base`)

## Query Plan

### 1. Server Setup
```
Use MCPM to search for filesystem and database servers
```

### 2. Installation
```
Install filesystem and sqlite servers, then add them to my config
```
*Restart Claude Desktop after this step*

### 3. Database Schema
```
Create a SQLite schema for storing document embeddings with fields for content, embedding vector, source file, and metadata
```

### 4. Document Processing
```
Read all markdown files from ~/Documents/knowledge-base and create a simple chunking function that splits them into 500-character chunks with 50 character overlap
```

### 5. Indexing
```
For each chunk, create a simple embedding by extracting key terms and concepts. Store these in our SQLite database with the chunk text and source information.
```

### 6. Query Function
```
Create a query function that takes a user question, finds the most relevant chunks based on term overlap, and returns the top 5 chunks with their source files
```

### 7. Terminal Interface
```
Create a simple terminal script that loops, accepts user questions, queries our RAG database, and formats the results nicely
```

## Expected Output
A working `rag_agent.py` that:
- Indexes your documents
- Accepts natural language queries
- Returns relevant chunks with sources
- Runs entirely in your terminal

## Time Estimate
~10 minutes from start to working RAG agent

## Why This Works
MCPM handles the infrastructure (finding, installing, configuring servers) while Claude Code writes the implementation. This separation lets you focus on the application logic rather than setup and configuration.
