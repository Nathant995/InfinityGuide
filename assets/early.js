try { document.documentElement.dataset.theme = localStorage.getItem('infinity-theme') || 'dark'; } catch { document.documentElement.dataset.theme = 'dark'; }
