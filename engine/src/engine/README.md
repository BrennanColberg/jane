How does the engine work?

1.  takes an input (via API or CLI)
2.  generate initial prompt
3.  feed prompt into LLM
4.  if LLM "done" return
5.  else LLM called a tool, so invoke the tool
6.       append tool's output to prompt
7.       GOTO 3
