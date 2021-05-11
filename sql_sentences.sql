SELECT l.idbot, b.phonenumber, b.apiid, b.apihash, l.balance FROM public."LastBalanceByBot" l inner join bots b on l.idbot = b.idbot left join botsuspend s on l.idbot = s.idbotsuspend where l.idbot >= 1 and l.idbot <= 12 and s.idbotsuspend is null  UNION ALL SELECT l.idbot, b.phonenumber, b.apiid, b.apihash, l.balance FROM public."LastBalanceByBot" l inner join bots b on l.idbot = b.idbot left join botsuspend s on l.idbot = s.idbotsuspend where l.idbot >= 13 and l.idbot <= 400 and l.balance > 0.000225 and s.idbotsuspend is null ORDER BY balance DESC
SELECT l.idbot, b.phonenumber, b.apiid, b.apihash, l.balance FROM public."LastBalanceByBot" l inner join bots b on l.idbot = b.idbot left join botsuspend s on l.idbot = s.idbotsuspend where l.idbot >= 13 and l.idbot <= 400 and l.balance > 0.00015 and l.balance <= 0.000225 and s.idbotsuspend is null ORDER BY balance DESC
SELECT l.idbot, b.phonenumber, b.apiid, b.apihash, l.balance FROM public."LastBalanceByBot" l inner join bots b on l.idbot = b.idbot left join botsuspend s on l.idbot = s.idbotsuspend where l.idbot >= 13 and l.idbot <= 400 and l.balance > 0.000075 and l.balance <= 0.00015 and s.idbotsuspend is null ORDER BY balance DESC
SELECT l.idbot, b.phonenumber, b.apiid, b.apihash, l.balance FROM public."LastBalanceByBot" l inner join bots b on l.idbot = b.idbot left join botsuspend s on l.idbot = s.idbotsuspend where l.idbot >= 13 and l.idbot <= 400 and l.balance <= 0.000075 and s.idbotsuspend is null ORDER BY balance DESC
SELECT l.idbot, b.phonenumber, b.apiid, b.apihash, l.balance FROM public."LastBalanceByBot" l inner join bots b on l.idbot = b.idbot left join botsuspend s on l.idbot = s.idbotsuspend where l.idbot >= 401 and s.idbotsuspend is null ORDER BY balance DESC