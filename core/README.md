How does the engine work?

1.  takes an input (via API)
2.  generates initial prompt (or retrieves session history)
3.  feed prompt into LLM
4.  return LLM output

TODO change ending to:

4.  if LLM "done" return
5.  else LLM called a tool, so invoke the tool
6.        append tool's output to prompt
7.        GOTO 3
