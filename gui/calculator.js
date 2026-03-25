/**
 * Lógica de Tiempo para CalcTime GUI
 * Almacena el tiempo internamente en MINUTOS para mayor precisión.
 */
class Tiempo {
    static MINUTOS_POR_HORA = 60;
    static HORAS_POR_DIA = 24;
    static DIAS_POR_MES = 30;
    static MESES_POR_AÑO = 12;

    static MINUTOS_POR_DIA = Tiempo.MINUTOS_POR_HORA * Tiempo.HORAS_POR_DIA; // 1440
    static MINUTOS_POR_MES = Tiempo.MINUTOS_POR_DIA * Tiempo.DIAS_POR_MES; // 43200
    static MINUTOS_POR_AÑO = Tiempo.MINUTOS_POR_MES * Tiempo.MESES_POR_AÑO; // 518400

    constructor(años = 0, meses = 0, dias = 0, horas = 0, minutos = 0) {
        this.totalMinutos = (años * Tiempo.MINUTOS_POR_AÑO) +
                            (meses * Tiempo.MINUTOS_POR_MES) +
                            (dias * Tiempo.MINUTOS_POR_DIA) +
                            (horas * Tiempo.MINUTOS_POR_HORA) +
                            minutos;
    }

    obtenerComponentes() {
        let mins = Math.abs(this.totalMinutos);
        const signo = this.totalMinutos < 0 ? -1 : 1;

        const años = Math.floor(mins / Tiempo.MINUTOS_POR_AÑO);
        mins %= Tiempo.MINUTOS_POR_AÑO;

        const meses = Math.floor(mins / Tiempo.MINUTOS_POR_MES);
        mins %= Tiempo.MINUTOS_POR_MES;

        const dias = Math.floor(mins / Tiempo.MINUTOS_POR_DIA);
        mins %= Tiempo.MINUTOS_POR_DIA;

        const horas = Math.floor(mins / Tiempo.MINUTOS_POR_HORA);
        const minutos = mins % Tiempo.MINUTOS_POR_HORA;

        return {
            años: años * signo,
            meses: meses * signo,
            dias: dias * signo,
            horas: horas * signo,
            minutos: minutos * signo
        };
    }

    toString() {
        const comp = this.obtenerComponentes();
        const partes = [];
        
        if (comp.años !== 0) partes.push(`${comp.años}a`);
        if (comp.meses !== 0) partes.push(`${comp.meses}m`);
        if (comp.dias !== 0) partes.push(`${comp.dias}d`);
        if (comp.horas !== 0) partes.push(`${comp.horas}h`);
        if (comp.minutos !== 0 || partes.length === 0) partes.push(`${comp.minutos}min`);

        return partes.join(' ');
    }
}

/**
 * Gestor de la Calculadora
 */
const Calculator = {
    display: null,
    expression: '',
    currentValue: '0',
    lastResult: null,
    operator: null,
    
    // Estado interno para construir el objeto Tiempo actual
    tempValues: { años: 0, meses: 0, dias: 0, horas: 0, minutos: 0 },
    history: [],
    settings: {
        darkMode: true,
        font: "'Inter', sans-serif"
    },

    init() {
        this.display = document.getElementById('result');
        this.exprView = document.getElementById('expression');
        this.historyList = document.getElementById('history-list');
        
        this.loadData();
        this.applySettings();
        this.addEventListeners();
        this.renderHistory();
    },

    loadData() {
        const savedHistory = localStorage.getItem('calcTime_history');
        if (savedHistory) this.history = JSON.parse(savedHistory);

        const savedSettings = localStorage.getItem('calcTime_settings');
        if (savedSettings) this.settings = JSON.parse(savedSettings);
    },

    saveData() {
        localStorage.setItem('calcTime_history', JSON.stringify(this.history));
        localStorage.setItem('calcTime_settings', JSON.stringify(this.settings));
    },

    applySettings() {
        document.body.classList.toggle('light-mode', !this.settings.darkMode);
        document.getElementById('theme-toggle').checked = this.settings.darkMode;
        
        document.documentElement.style.setProperty('--display-font', this.settings.font);
        document.getElementById('font-select').value = this.settings.font;
    },

    addEventListeners() {
        // Botones del teclado
        document.querySelectorAll('.btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;
                const value = btn.textContent;
                this.handleInput(action, value);
            });
        });

        // Controles de Pantalla/Paneles
        document.getElementById('btn-history').onclick = () => this.togglePanel('history-panel', true);
        document.getElementById('btn-settings').onclick = () => this.togglePanel('settings-panel', true);
        document.getElementById('close-history').onclick = () => this.togglePanel('history-panel', false);
        document.getElementById('close-settings').onclick = () => this.togglePanel('settings-panel', false);

        // Controles de Ajustes
        document.getElementById('theme-toggle').onchange = (e) => {
            this.settings.darkMode = e.target.checked;
            this.applySettings();
            this.saveData();
        };

        document.getElementById('font-select').onchange = (e) => {
            this.settings.font = e.target.value;
            this.applySettings();
            this.saveData();
        };

        // Acciones de Historial
        document.getElementById('clear-history').onclick = () => {
            if (confirm('¿Vaciar todo el historial?')) {
                this.history = [];
                this.renderHistory();
                this.saveData();
            }
        };

        document.getElementById('export-btn').onclick = () => this.exportHistory();

        // Soporte de teclado básico
        document.addEventListener('keydown', (e) => {
            if (e.key >= '0' && e.key <= '9') this.handleInput('digit', e.key);
            if (e.key === '+') this.handleInput('operator', '+');
            if (e.key === '-') this.handleInput('operator', '-');
            if (e.key === 'Enter') this.handleInput('calculate');
            if (e.key === 'Escape') {
                this.handleInput('clear');
                this.togglePanel('history-panel', false);
                this.togglePanel('settings-panel', false);
            }
        });
    },

    togglePanel(id, show) {
        document.getElementById(id).classList.toggle('active', show);
    },

    handleInput(action, value) {
        switch(action) {
            case 'digit':
                if (value === '.') {
                    if (!this.currentValue.includes('.')) this.currentValue += '.';
                } else if (this.currentValue === '0') {
                    this.currentValue = value;
                } else {
                    this.currentValue += value;
                }
                this.updateDisplay();
                break;

            case 'delete':
                if (this.currentValue.length > 1) {
                    this.currentValue = this.currentValue.slice(0, -1);
                } else {
                    this.currentValue = '0';
                }
                this.updateDisplay();
                break;
            
            case 'unit':
                const num = parseFloat(this.currentValue);
                const unitMap = { 'Años': 'años', 'Meses': 'meses', 'Días': 'dias', 'Horas': 'horas', 'Minutos': 'minutos' };
                this.tempValues[unitMap[value]] = num;
                
                const unitDisplay = { 'Años': 'a', 'Meses': 'm', 'Días': 'd', 'Horas': 'h', 'Minutos': 'min' }[value];
                this.expression += `${num}${unitDisplay} `;
                this.currentValue = '0';
                this.updateDisplay();
                break;

            case 'operator':
                const t = new Tiempo(
                    this.tempValues.años, this.tempValues.meses, this.tempValues.dias,
                    this.tempValues.horas, this.tempValues.minutos
                );
                
                if (!this.lastResult) this.lastResult = t;
                else if (this.operator) this.calculateIntermediate(t);
                
                this.operator = value;
                this.expression += ` ${value} `;
                this.resetTempValues();
                this.updateDisplay();
                break;

            case 'calculate':
                const finalT = new Tiempo(
                    this.tempValues.años, this.tempValues.meses, this.tempValues.dias,
                    this.tempValues.horas, this.tempValues.minutos
                );
                if (this.lastResult && this.operator) {
                    const prevStr = this.lastResult.toString();
                    this.calculateIntermediate(finalT);
                    const resultStr = this.lastResult.toString();
                    
                    this.addToHistory(`${prevStr} ${this.operator} ${finalT.toString()} = ${resultStr}`);
                    
                    this.expression = '';
                    this.operator = null;
                    this.resetTempValues();
                    this.updateDisplay(true);
                }
                break;

            case 'clear':
                this.expression = '';
                this.currentValue = '0';
                this.lastResult = null;
                this.operator = null;
                this.resetTempValues();
                this.updateDisplay();
                break;

            case 'copy':
                const textToCopy = this.lastResult ? this.lastResult.toString() : this.currentValue;
                navigator.clipboard.writeText(textToCopy);
                // Mini feedback (opcional, alert es intrusivo)
                const originalText = this.display.textContent;
                this.display.textContent = '¡Copiado!';
                setTimeout(() => this.display.textContent = originalText, 1000);
                break;
        }
    },

    calculateIntermediate(t) {
        if (this.operator === '+') {
            this.lastResult.totalMinutos += t.totalMinutos;
        } else if (this.operator === '-') {
            this.lastResult.totalMinutos -= t.totalMinutos;
        } else if (this.operator === '×') {
            // Multiplicación por escalar
            const escalar = parseFloat(this.currentValue) || 1;
            this.lastResult.totalMinutos *= escalar;
        } else if (this.operator === '÷') {
            const escalar = parseFloat(this.currentValue) || 1;
            if (escalar !== 0) this.lastResult.totalMinutos /= escalar;
        }
    },

    resetTempValues() {
        this.tempValues = { años: 0, meses: 0, dias: 0, horas: 0, minutos: 0 };
        this.currentValue = '0';
    },

    addToHistory(entry) {
        const timestamp = new Date().toLocaleString();
        this.history.unshift({ entry, timestamp });
        if (this.history.length > 50) this.history.pop();
        this.renderHistory();
        this.saveData();
    },

    renderHistory() {
        this.historyList.innerHTML = this.history.length === 0 
            ? '<p style="text-align:center; opacity:0.5; margin-top:20px;">No hay historial</p>'
            : this.history.map(item => `
                <div class="history-item">
                    <div style="font-size:0.7rem; color:var(--text-secondary); margin-bottom:5px;">${item.timestamp}</div>
                    <div>${item.entry}</div>
                </div>
            `).join('');
    },

    exportHistory() {
        if (this.history.length === 0) return alert('No hay historial para exportar');
        
        const content = this.history.map(h => `[${h.timestamp}] ${h.entry}`).join('\n');
        const blob = new Blob([content], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'historial_calctime.txt';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    },

    updateDisplay(showResult = false) {
        this.exprView.textContent = this.expression;
        if (showResult && this.lastResult) {
            this.display.textContent = this.lastResult.toString();
        } else {
            this.display.textContent = this.currentValue;
        }
    }
};

window.onload = () => Calculator.init();
