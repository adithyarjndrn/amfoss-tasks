package main

import (
	"encoding/csv"
	"log"
	"os"

	"github.com/gocolly/colly"
)

func main() {
	fName := "data.csv"
	file, err := os.Create(fName)
	if err != nil {
		log.Fatalf("Could not create file, err:%q", err)
		return
	}
	defer file.Close()
	writer := csv.NewWriter(file)
	defer writer.Flush()
	c := colly.NewCollector(
		colly.AllowedDomains("https://www.forbes.com/real-time-billionaires"),
	)
	c.OnHTML(".fbs-table", func(e *colly.HTMLElement) {
		writer.Write([]string{
			e.ChildText("a"),
		})
	})
	log.Printf("Scraping Complete")
	log.Print(c)
}
