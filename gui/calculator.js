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
    activeUnit: null,

    init() {
        this.display = document.getElementById('result');
        this.exprView = document.getElementById('expression');
        this.addEventListeners();
    },

    addEventListeners() {
        document.querySelectorAll('.btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;
                const value = btn.textContent;
                this.handleInput(action, value);
            });
        });

        // Soporte de teclado básico
        document.addEventListener('keydown', (e) => {
            if (e.key >= '0' && e.key <= '9') this.handleInput('digit', e.key);
            if (e.key === '+') this.handleInput('operator', '+');
            if (e.key === '-') this.handleInput('operator', '-');
            if (e.key === 'Enter') this.handleInput('calculate');
            if (e.key === 'Escape') this.handleInput('clear');
        });
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
                const num = parseInt(this.currentValue);
                const unitMap = { 'Años': 'años', 'Meses': 'meses', 'Días': 'dias', 'Horas': 'horas', 'Minutos': 'minutos' };
                this.tempValues[unitMap[value]] = num;
                
                // Representación visual
                const unitDisplay = { 'Años': 'a', 'Meses': 'm', 'Días': 'd', 'Horas': 'h', 'Minutos': 'min' }[value];
                this.expression += `${num}${unitDisplay} `;
                this.currentValue = '0';
                this.updateDisplay();
                break;

            case 'operator':
                // Si hay valores temporales, construir un Tiempo
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
                    
                    // Agregar al historial
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
                alert('¡Copiado al portapapeles!');
                break;
        }
    },

    calculateIntermediate(t) {
        if (this.operator === '+') {
            this.lastResult.totalMinutos += t.totalMinutos;
        } else if (this.operator === '-') {
            this.lastResult.totalMinutos -= t.totalMinutos;
        }
        // Multiplicación y división funcionalmente diferentes (requieren escalar)
        // Se implementarán en la siguiente fase
    },

    resetTempValues() {
        this.tempValues = { años: 0, meses: 0, dias: 0, horas: 0, minutos: 0 };
        this.currentValue = '0';
    },

    addToHistory(entry) {
        console.log("Historial:", entry);
        // Podríamos renderizar esto en un panel lateral
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
