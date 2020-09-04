# TACC CMS Per-Site Assets - Snippets

This directory allows us to manually save snippet code.

This can alleviate danger #1 of [Why a Snippet Is Dangerous](#why-a-snippet-is-dangerous).

## Usage

> __Important__: The Core CMS __must not__ use any Snippets, _ever_!

In a branded project (a.k.a. repo fork):

1. Any CMS Snippet __must__ also be saved into this directory in its own file.
2. Any snippet file __must__ be kept up to date. (Manage via team process.)

## What a Snippet Is

A __dangerous__ plugin [`djangocms-snippet`](https://github.com/divio/djangocms-snippet) is installed in our CMS.

It allows an authorized CMS user to create a snippet of front-end web code (i.e. CSS, HTML, JS) in the database for use anywhere on the website.

## Why a Snippet Is Dangerous

It is __dangerous__ because:

1. The code is not version-controlled, thus dependent on the (unsynced) database.
2. The code is independent of any code control:
    - security
    - dependency management
    - style guide
    - organization
    - linting

## Why a Snippet Is Allowed

1. Support time-sensitive changes to the CMS.\*
2. Support ad-hoc changes by designer who codes.\*

\* Until those changes can be appropriately integrated into the repository.
