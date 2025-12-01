/**
 * BLOG TÉCNICO: GRAFOS
 * Script Principal - Funcionalidades Interactivas
 * Características: Tema oscuro/claro, Navegación, Demostraciones de Algoritmos
 */

// ============================================
// 1. GESTIÓN DE TEMA OSCURO/CLARO
// ============================================

const themeToggle = document.getElementById('themeToggle');
const body = document.body;

/**
 * Inicializa el tema guardado en localStorage
 */
function initTheme() {
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    let isDarkMode = savedTheme ? savedTheme === 'dark' : prefersDark;
    
    if (isDarkMode) {
        enableDarkMode();
    } else {
        enableLightMode();
    }
}

function enableDarkMode() {
    body.classList.add('dark-mode');
    localStorage.setItem('theme', 'dark');
    updateThemeIcon();
}

function enableLightMode() {
    body.classList.remove('dark-mode');
    localStorage.setItem('theme', 'light');
    updateThemeIcon();
}

function toggleTheme() {
    if (body.classList.contains('dark-mode')) {
        enableLightMode();
    } else {
        enableDarkMode();
    }
}

function updateThemeIcon() {
    const isDark = body.classList.contains('dark-mode');
    if (themeToggle) {
        themeToggle.textContent = isDark ? '☀️' : '🌙';
    }
}

// ============================================
// 2. EVENTOS Y LISTENERS
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar tema
    initTheme();
    
    // Listeners para cambio de tema
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
    
    // Smooth scroll para links internos
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});

// ============================================
// 3. FUNCIONES DE DEMOSTRACIÓN DE ALGORITMOS
// ============================================

/**
 * BFS (Búsqueda en Amplitud)
 */
function demonstrateBFS() {
    const adjacencyList = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    };
    const result = simulateBFS('A', adjacencyList);
    displaySearchResult('bfs-result', result, 'BFS');
}

/**
 * DFS (Búsqueda en Profundidad)
 */
function demonstrateDFS() {
    const adjacencyList = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    };
    const result = simulateDFS('A', adjacencyList);
    displaySearchResult('dfs-result', result, 'DFS');
}

/**
 * BFS - Implementación
 */
function simulateBFS(startNode, adjacencyList) {
    const visited = new Set();
    const queue = [startNode];
    const result = [];
    
    while (queue.length > 0) {
        const node = queue.shift();
        
        if (!visited.has(node)) {
            visited.add(node);
            result.push(node);
            
            if (adjacencyList[node]) {
                adjacencyList[node].forEach(neighbor => {
                    if (!visited.has(neighbor)) {
                        queue.push(neighbor);
                    }
                });
            }
        }
    }
    
    return result;
}

/**
 * DFS - Implementación
 */
function simulateDFS(startNode, adjacencyList, visited = new Set(), result = []) {
    visited.add(startNode);
    result.push(startNode);
    
    if (adjacencyList[startNode]) {
        adjacencyList[startNode].forEach(neighbor => {
            if (!visited.has(neighbor)) {
                simulateDFS(neighbor, adjacencyList, visited, result);
            }
        });
    }
    
    return result;
}

/**
 * Mostrar resultado de búsqueda
 */
function displaySearchResult(resultId, result, algorithm) {
    const resultElement = document.getElementById(resultId);
    if (resultElement) {
        resultElement.innerHTML = `<strong>${algorithm}:</strong> ${result.join(' → ')}`;
        resultElement.style.display = 'block';
    }
}
