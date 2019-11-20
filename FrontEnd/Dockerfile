FROM mcr.microsoft.com/dotnet/core/sdk:3.0-buster AS build
WORKDIR /src
COPY RetinopathyClassification_Blazor/RetinopathyClassification_Blazor.csproj .
RUN dotnet restore "RetinopathyClassification_Blazor.csproj"
COPY . .
RUN dotnet build "RetinopathyClassification_Blazor/RetinopathyClassification_Blazor.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "RetinopathyClassification_Blazor/RetinopathyClassification_Blazor.csproj" -c Release -o /app/publish

FROM nginx:alpine AS final
WORKDIR /usr/share/nginx/html
COPY --from=publish /app/publish/RetinopathyClassification_Blazor/dist .
COPY nginx.conf /etc/nginx/nginx.conf