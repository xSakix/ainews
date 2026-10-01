{{- /* <page URL>index.md — the page as clean Markdown for LLMs and AI tools. */ -}}
# {{ .Title }}
{{ with .Description }}
> {{ . }}
{{ end }}
- URL: {{ .Permalink }}
{{- if not .Date.IsZero }}
- Published: {{ .Date.Format "2006-01-02" }}
{{- end }}
{{- with .Params.tags }}
- Tags: {{ delimit . ", " }}
{{- end }}
- Publisher: [{{ site.Title }}]({{ site.Home.Permalink }})

{{ .RawContent | replaceRE `\{\{[<%].*?[>%]\}\}` "" | strings.TrimSpace }}
