const STALE_THRESHOLD = 60 * 60; // 1 giờ

function checkDataFreshness(data) {
    if (!data || data.length === 0) return { isStale: true, ageSeconds: 0 };

    let latestTimestamp = null;
    for (let item of data) {
        const ts = item.processing_timestamp || item.timestamp || item.kafka_timestamp;
        if (ts) {
            const timeString = ts.endsWith('Z') ? ts : ts + 'Z';
            const date = new Date(timeString);
            if (!latestTimestamp || date > latestTimestamp) {
                latestTimestamp = date;
            }
        }
    }

    if (!latestTimestamp) return { isStale: true, ageSeconds: 0 };

    const nowLocal = new Date();
    console.log("Thời gian hiện tại (Local):", nowLocal.toString());

    const nowUTC = new Date(nowLocal.toISOString());
    console.log("Thời gian hiện tại (UTC):", nowUTC.toUTCString());

    const ageSeconds = (nowUTC - latestTimestamp) / 1000;

    return {
        isStale: ageSeconds > STALE_THRESHOLD,
        ageSeconds: ageSeconds,
        latestTimestamp: latestTimestamp,
        nowLocal: nowLocal,
        nowUTC: nowUTC
    };
}

// Test với dữ liệu giả
const testData = [
    { timestamp: "2025-11-20T10:00:00" }, 
];

const result = checkDataFreshness(testData);
console.log("Kết quả:", result);