# single source of truth for the installed version — `-v`, `version` and
# `upgrade` all read it. bump it in the same change you tag a release with;
# the release workflow refuses to build if the tag and this don't match.
VERSION = "1.0.1"
