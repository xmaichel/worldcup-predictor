.PHONY: sync status

sync:   ## Pull → Commit → Push
	@bash sync.sh

status: ## Ver estado del repo
	@echo "📊 Status:"
	@git status --short 2>/dev/null
	@echo ""
	@echo "📅 Último commit:"
	@git log --oneline -1 2>/dev/null
	@echo ""
	@echo "🔗 Remote:"
	@git remote -v 2>/dev/null

backup: ## Alias de sync
	@bash sync.sh
