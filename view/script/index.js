$(function () {
    initControllerEvents()    
    
    
    
})

const initControllerEvents = () => {
    const app = $('#app')
    const baseUrl = 'http://127.0.0.1:5000'
    const getMystatJsonUrl = '/mystat/json'
    const getMystatExpensesImgUrl = '/mystat/expenses/chart.png'

    loadMystatJsonEvent(app, baseUrl + getMystatJsonUrl)
    loadExpensesChart(app, baseUrl + getMystatExpensesImgUrl)
    loadMystatTable(app, baseUrl + getMystatJsonUrl + `?addSleepDuration=1`)
}

const loadMystatJsonEvent = (app, apiUrl) => {
    $('#mystat-json').click((e) => {
        showPreloader()
        
        $.ajax({
            dataType: 'json',
            url: apiUrl,
            method: 'GET',
        }).done((response) => {
            // console.log(response);
            app.html("<pre>" + JSON.stringify(response, undefined, 4) + "</pre>")
        }).always(hidePreloader)
    })
}

const loadMystatTable = (app, apiUrl) => {
    $('#mystat-table').click((e) => {
        showPreloader()
        
        $.ajax({
            dataType: 'json',
            url: apiUrl,
        }).done((response) => {
            // console.log(response);
            if (!response || !response.length) return
            
            let html = `
            <table class="table">
                <thead>
                    <tr>
            `
            Object.keys(response[0]).forEach((key) => {
                html += `<th scope="col">${key}</th>`
            })
            html += `
                    </tr>
                </thead>
            <tbody class="table-group-divider">
            `
            response.forEach((record) => {
                html += '<tr>'
                Object.values(record).forEach((val, id) => {
                    html += id == 0 ? `<th scope="row">${val}</th>` : `<td>${val}</td>`
                })
                html += '</tr>'
            })
            html += `
                </tbody>
            </table>
            `

            app.html(html)
        }).always(hidePreloader)
    })
}

const loadExpensesChart = (app, apiUrl) => {    
    $('#expenses-chart').click((e) => {
        app.html(`<img src="${apiUrl}" alt="Expenses Chart" height="95%" style="display: block; margin: auto;" />`)
    })
}

const showPreloader = () => {
    $('#preloader').css('display', 'flex')
}

const hidePreloader = () => {
    $('#preloader').css('display', 'none')
}