WITH CustosCampanha AS (
    SELECT
        canal_aquisicao,
        id_campanha,
        SUM(investimento) AS total_investido,
        SUM(cliques) AS total_cliques
    FROM marketing_spend_data
    WHERE data_campanha BETWEEN '2026-01-01' AND '2026-03-31'
    GROUP BY canal_aquisicao, id_campanha
),
ReceitaCampanha AS (
    SELECT
        u.id_campanha,
        COUNT(DISTINCT t.id_transacao) AS total_conversoes,
        SUM(t.valor_receita) AS receita_gerada
    FROM dim_usuarios u
    JOIN fato_transacoes t ON u.id_usuario = t.id_usuario
    WHERE t.status_pagamento = 'Aprovado'
    GROUP BY u.id_campanha
)
SELECT
    c.canal_aquisicao,
    c.id_campanha,
    c.total_investido,
    COALESCE(r.receita_gerada, 0) AS receita_gerada,
    COALESCE(r.total_conversoes, 0) AS total_conversoes,
    (COALESCE(r.receita_gerada, 0) - c.total_investido) AS lucro_bruto,
    ROUND((COALESCE(r.receita_gerada, 0) - c.total_investido) / NULLIF(c.total_investido, 0) * 100, 2) AS roi_percentual,
    RANK() OVER (ORDER BY (COALESCE(r.receita_gerada, 0) - c.total_investido) DESC) as ranking_lucratividade
FROM CustosCampanha c
LEFT JOIN ReceitaCampanha r ON c.id_campanha = r.id_campanha
ORDER BY ranking_lucratividade;
