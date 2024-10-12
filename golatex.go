package main

import (
    "os"
    "github.com/jesuino/golatex"
)

func main() {
    doc := golatex.NewDocument()
    doc.Add(golatex.NewSection("Hello, LaTeX!"))
    doc.Add(golatex.NewParagraph("This is an example of using LaTeX in Go."))
    os.WriteFile("output.tex", []byte(doc.String()), 0644)
}
