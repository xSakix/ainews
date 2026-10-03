+++
title = "turbopuffer demotes its vector index to speed other queries"
description = "An engineering account explains why a layout built around similarity search constrains other database operations."
tags = ["essays", "tools"]
date = 2026-10-03T05:48:20+02:00
draft = false
+++

turbopuffer, a search database provider, is redesigning its storage so the vector index becomes a secondary index, engineer Dan Harrison wrote on September 30.

The company originally organised documents around groups of similar vectors, the numerical representations used to find related content. That arrangement served similarity search well. Harrison says it now restricts other ways of querying the same documents.

**Why it matters:** A developer building a search application needs keyword searches, filters and summaries to work efficiently alongside semantic retrieval. Harrison's account shows how the physical arrangement of records can make those operations compete with the database's original purpose.

His explanation centres on the address used to store a document. In the current design, that address follows its position in the vector index. Rearranging vectors therefore moves associated document data and indexes too. Adding several vectors to one document can also duplicate its contents.

Different query operations prefer different sizes of data block. Harrison argues that forcing them all to follow the similarity clusters prevents each operation from choosing its own efficient layout. This is an engineering argument about the structure underneath the query, rather than about replacing vector search itself.

The proposed separation gives the vector index a narrower responsibility: pointing to documents instead of governing where every part of them lives. For a search engineer, that is a useful question to ask of an architecture review: which component owns the document, and which components merely locate it? The distinction remains meaningful even when the database provides a single query interface.

Harrison says the new version has passed the company's correctness tests. Public performance measurements and a production rollout remain ahead; the company plans to share benchmarks over the coming weeks.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Harrison, publication date, current layout and proposed secondary vector index. | VENDOR-REPORTED | https://turbopuffer.com/blog/rip-vector-database | None; attributed primary account. |
| Moving vectors moves related records; multiple vectors duplicate content; query block sizes differ. | VENDOR-REPORTED | https://turbopuffer.com/blog/rip-vector-database | None; attributed primary account. |
| Separating record ownership from lookup is useful in architecture review. | ANALYSIS | https://turbopuffer.com/blog/rip-vector-database | None; attributed primary account. |
| Correctness tests passed; benchmarks and rollout remain forthcoming. | VENDOR-REPORTED | https://turbopuffer.com/blog/rip-vector-database | None; attributed primary account. |
